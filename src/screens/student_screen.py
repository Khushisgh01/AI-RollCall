import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image
import numpy as np
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject
import time

from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card

STUDENT_STYLES = """
<style>
@keyframes welcomeIn {
    from { opacity: 0; transform: scale(0.9); }
    to   { opacity: 1; transform: scale(1); }
}
.welcome-banner {
    background: linear-gradient(135deg, #5865F2 0%, #7c3aed 50%, #EB459E 100%);
    border-radius: 20px;
    padding: 20px 24px;
    color: white;
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 1rem;
    box-shadow: 0 8px 30px rgba(88,101,242,0.25);
    animation: welcomeIn 0.5s cubic-bezier(0.34,1.56,0.64,1) both;
}
.welcome-avatar {
    width: 48px; height: 48px;
    background: rgba(255,255,255,0.2);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.4rem;
    flex-shrink: 0;
}
.welcome-name {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 1.1rem;
    margin: 0;
}
.welcome-sub {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.8rem;
    opacity: 0.75;
    margin: 2px 0 0;
}
.scan-hint {
    background: linear-gradient(135deg, rgba(88,101,242,0.06), rgba(235,69,158,0.04));
    border: 1px solid rgba(88,101,242,0.12);
    border-radius: 16px;
    padding: 16px 20px;
    text-align: center;
    margin: 1rem 0;
}
.scan-hint-icon { font-size: 2rem; margin-bottom: 6px; }
.scan-hint-text {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.88rem;
    color: #5865F2;
    font-weight: 500;
}
.section-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 1.5rem 0 0.5rem;
}
.section-pill {
    background: linear-gradient(135deg, #5865F2, #EB459E);
    color: white;
    font-family: 'DM Sans', sans-serif;
    font-weight: 600;
    font-size: 0.75rem;
    padding: 3px 10px;
    border-radius: 20px;
    letter-spacing: 0.05em;
}
</style>
"""


def student_dashboard():
    st.markdown(STUDENT_STYLES, unsafe_allow_html=True)

    student_data = st.session_state.student_data
    student_id = student_data['student_id']

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.markdown(f"""
            <div class="welcome-banner">
                <div class="welcome-avatar">👋</div>
                <div>
                    <div class="welcome-name">{student_data['name']}</div>
                    <div class="welcome-sub">Student Dashboard</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data
            st.rerun()

    st.space()

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="section-header"><h3 style="margin:0">Your Subjects</h3><span class="section-pill">enrolled</span></div>', unsafe_allow_html=True)
    with c2:
        if st.button('+ Enroll in Subject', type='primary', width='stretch'):
            enroll_dialog()

    st.divider()

    with st.spinner('Loading your subjects…'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}
    for log in logs:
        sid = log['subject_id']
        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}
        stats_map[sid]['total'] += 1
        if log.get('is_present'):
            stats_map[sid]['attended'] += 1

    if not subjects:
        st.markdown("""
            <div style="text-align:center; padding: 3rem; background: white; border-radius: 20px; border: 1px solid rgba(88,101,242,0.1)">
                <div style="font-size:3rem; margin-bottom:12px">📚</div>
                <div style="font-family:'Syne',sans-serif; font-weight:700; color:#1a1a2e; font-size:1.1rem">No subjects yet</div>
                <div style="font-family:'DM Sans',sans-serif; color:#6b7280; font-size:0.88rem; margin-top:4px">Enroll in a subject using the button above</div>
            </div>
        """, unsafe_allow_html=True)
    else:
        cols = st.columns(2)
        for i, sub_node in enumerate(subjects):
            sub = sub_node['subjects']
            sid = sub['subject_id']
            stats = stats_map.get(sid, {"total": 0, "attended": 0})
            with cols[i % 2]:
                subject_card(
                    name=sub['name'],
                    code=sub['subject_code'],
                    section=sub['section'],
                    stats=[
                        ('📅', 'Total', stats['total']),
                        ('✅', 'Attended', stats['attended']),
                    ],
                )
                if st.button("🗑️ Unenroll", type='tertiary', width='stretch', key=f"unenroll_{sid}"):
                    unenroll_student_to_subject(student_id, sid)
                    st.toast(f"Unenrolled from {sub['name']}")
                    st.rerun()

    footer_dashboard()


def student_screen():
    style_background_dashboard()
    style_base_layout()
    st.markdown(STUDENT_STYLES, unsafe_allow_html=True)

    if "student_data" in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("← Back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.markdown("""
        <div style="text-align:center; margin: 1.5rem 0 0.5rem">
            <div style="font-family:'Syne',sans-serif; font-weight:800; font-size:1.6rem; color:#1a1a2e; margin-bottom:4px">
                Face ID Login
            </div>
            <div style="font-family:'DM Sans',sans-serif; font-size:0.9rem; color:#6b7280">
                Position your face in the center of the camera
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="scan-hint">
            <div class="scan-hint-icon">🎯</div>
            <div class="scan-hint-text">Look directly at the camera for best results</div>
        </div>
    """, unsafe_allow_html=True)

    show_registration = False
    photo_source = st.camera_input("Take a photo to login", label_visibility='collapsed')

    if photo_source:
        img = np.array(Image.open(photo_source))
        with st.spinner('🤖 AI is scanning your face…'):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning('😕 No face detected — please try again in better lighting')
            elif num_faces > 1:
                st.warning('👥 Multiple faces found — please ensure only you are in frame')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id'] == student_id), None)
                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f"Welcome back, {student['name']}! 🎉")
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info('👋 Face not recognized — you might be new here!')
                    show_registration = True

    if show_registration:
        st.markdown("""
            <div style="margin-top:1.5rem">
                <div style="font-family:'Syne',sans-serif; font-weight:700; font-size:1.3rem; color:#1a1a2e; margin-bottom:4px">✨ Create your profile</div>
                <div style="font-family:'DM Sans',sans-serif; font-size:0.85rem; color:#6b7280; margin-bottom:1rem">Set up your AI RollCall account with face + optional voice</div>
            </div>
        """, unsafe_allow_html=True)

        with st.container(border=True):
            new_name = st.text_input("Your full name", placeholder='E.g. Priya Sharma')

            st.markdown("""
                <div style="margin:1rem 0 0.5rem">
                    <span style="font-family:'Syne',sans-serif; font-weight:600; font-size:0.9rem; color:#5865F2">🎙️ Voice Enrollment</span>
                    <span style="font-family:'DM Sans',sans-serif; font-size:0.78rem; color:#9ca3c4; margin-left:8px">optional</span>
                </div>
                <div style="font-family:'DM Sans',sans-serif; font-size:0.83rem; color:#6b7280; margin-bottom:8px">
                    Record yourself saying "I am present" or your name for voice attendance
                </div>
            """, unsafe_allow_html=True)

            audio_data = None
            try:
                audio_data = st.audio_input('Record a short phrase')
            except Exception:
                st.error('Audio recording unavailable')

            if st.button('🚀 Create My Account', type='primary', width='stretch'):
                if new_name:
                    with st.spinner('Creating your profile…'):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()
                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)
                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f"Welcome to AI RollCall, {new_name}! 🎉")
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error('Could not capture facial features — please retake the photo')
                else:
                    st.warning('Please enter your name')

    footer_dashboard()