# import streamlit as st

# from src.ui.base_layout import style_background_dashboard, style_base_layout

# from src.components.header import header_dashboard
# from src.components.footer import footer_dashboard
# from src.components.subject_card import subject_card
# from src.database.db import check_teacher_exists, create_teacher, teacher_login, get_teacher_subjects, get_attendance_for_teacher
# from src.components.dialog_create_subject import create_subject_dialog
# from src.components.dialog_share_subject import share_subject_dialog
# from src.components.dialog_add_photo import add_photos_dialog

# from src.pipelines.face_pipeline import predict_attendance
# from src.components.dialog_attendance_results import attendance_result_dialog
# import numpy as np

# from datetime import datetime

# import pandas as pd

# from src.database.config import supabase


# from src.components.dialog_voice_attendance import voice_attendance_dialog
# def teacher_screen():

#     style_background_dashboard()
#     style_base_layout()

#     if "teacher_data" in st.session_state:
#         teacher_dashboard()
#     elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=="login":
#         teacher_screen_login()
#     elif st.session_state.teacher_login_type == "register":
#         teacher_screen_register()





# def teacher_dashboard():
#     teacher_data = st.session_state.teacher_data
#     c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
#     with c1:
#         header_dashboard()
#     with c2:
#         st.subheader(f"""Welcome, {teacher_data['name']} """)
#         if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
#             st.session_state['is_logged_in'] = False
#             del st.session_state.teacher_data 
#             st.rerun()


#     st.space()

#     if "current_teacher_tab" not in st.session_state:
#         st.session_state.current_teacher_tab = 'take_attendance'
#     tab1, tab2, tab3 = st.columns(3)


#     with tab1:
#         type1 = "primary" if st.session_state.current_teacher_tab == 'take_attendance' else "tertiary"
#         if st.button('Take Attendance',type=type1, width='stretch', icon=':material/ar_on_you:'):
#             st.session_state.current_teacher_tab = 'take_attendance'
#             st.rerun()

#     with tab2:
#         type2 = "primary" if st.session_state.current_teacher_tab == 'manage_subjects' else "tertiary"
#         if st.button('Manage Subjects', type=type2, width='stretch', icon=':material/book_ribbon:'):
#             st.session_state.current_teacher_tab = 'manage_subjects'
#             st.rerun()

#     with tab3:
#         type3 = "primary" if st.session_state.current_teacher_tab == 'attendance_records' else "tertiary"
#         if st.button('Attendance Records',type=type3, width='stretch', icon=':material/cards_stack:'):
#             st.session_state.current_teacher_tab = 'attendance_records'
#             st.rerun()


#     st.divider()

#     if st.session_state.current_teacher_tab == "take_attendance":
#         teacher_tab_take_attendance()
#     if st.session_state.current_teacher_tab == "manage_subjects":
#         teacher_tab_manage_subjects()
#     if st.session_state.current_teacher_tab == "attendance_records":
#         teacher_tab_attendance_records()

    


#     footer_dashboard()

# def teacher_tab_take_attendance():
#     teacher_id = st.session_state.teacher_data['teacher_id']
#     st.header('Take AI Attendance')


#     if 'attendance_images' not in st.session_state:
#         st.session_state.attendance_images = []

#     subjects = get_teacher_subjects(teacher_id)

#     if not subjects:
#         st.warning('You havent created any subjects yet! Please create one to begin!')
#         return
    
#     subject_options = {f"{s['name']} - {s['subject_code']}": s['subject_id'] for s in subjects}

#     col1, col2 = st.columns([3,1], vertical_alignment='bottom')

#     with col1:
#         selected_subject_label = st.selectbox('Select Subject', options=list(subject_options.keys()))

#     with col2:
#         if st.button('Add Photos', type='primary', icon=':material/photo_prints:', width='stretch'):
#             add_photos_dialog()

#     selected_subject_id = subject_options[selected_subject_label]

#     st.divider()

#     if st.session_state.attendance_images:
#         st.header('Added Photos')
#         gallery_cols = st.columns(4)

#         for idx, img in enumerate(st.session_state.attendance_images):
#             with gallery_cols[idx % 4 ]:
#                 st.image(img, width='stretch', caption=f'Photo {idx+1}')
#     has_photos = bool(st.session_state.attendance_images)
#     c1, c2, c3 = st.columns(3)

#     with c1:
#         if st.button('Clear all photos', width='stretch', type='tertiary', icon=':material/delete:', disabled=not has_photos):
#             st.session_state.attendance_images = []
#             st.rerun()


#     with c2:
        
#         if st.button('Run Face Analysis', width='stretch', type='secondary', icon=':material/analytics:', disabled=not has_photos):
#             with st.spinner('Deep scanning classroom photos...'):
#                 all_detected_ids = {}

#                 for idx, img in enumerate(st.session_state.attendance_images):
#                     img_np = np.array(img.convert('RGB'))
#                     detected, _, _ = predict_attendance(img_np)


#                     if detected:
#                         for sid in detected.keys():
#                             student_id = int(sid)

#                             all_detected_ids.setdefault(student_id, []).append(f"Photo {idx+1}")

#                 enrolled_res = supabase.table('subject_students').select("*, students(*)").eq('subject_id',selected_subject_id ).execute()
#                 enrolled_students = enrolled_res.data

#                 if not enrolled_students:
#                     st.warning('No students enrolled in this course')
#                 else:

#                     results, attendance_to_log  = [], []

#                     current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


#                     for node in enrolled_students:
#                         student = node['students']
#                         sources = all_detected_ids.get(int(student['student_id']), [])
#                         is_present= len(sources) > 0

#                         results.append({
#                             "Name": student['name'],
#                             "ID": student['student_id'],
#                             "Source": ", ".join(sources) if is_present else "-",
#                             "Status": "✅ Present" if is_present else "❌ Absent"
#                         })

#                         attendance_to_log.append({
#                             'student_id': student['student_id'],
#                             'subject_id': selected_subject_id,
#                             'timestamp': current_timestamp,
#                             'is_present': bool(is_present)
#                         })

#                 attendance_result_dialog(pd.DataFrame(results), attendance_to_log)

#     with c3:
#         if st.button('Use Voice Attendance', type='primary', width='stretch', icon=':material/mic:'):
#             voice_attendance_dialog(selected_subject_id)











# def teacher_tab_manage_subjects():
#     teacher_id = st.session_state.teacher_data['teacher_id']
#     col1, col2 = st.columns(2)
#     with col1:
#         st.header('Manage Subjects', width='stretch')

#     with col2:
#         if st.button('Create New Subject', width='stretch'):
#             create_subject_dialog(teacher_id)


#     # LIST all SUBJECTS
#     subjects = get_teacher_subjects(teacher_id)
#     if subjects:
#         for sub in subjects:
#             stats = [
#                 ("🫂", "Students", sub['total_students']),
#                 ("🕰️", "Classes", sub['total_classes']),
#             ]
#         def share_btn():
#             if st.button(f"Share Code: {sub['name']}", key=f"share_{sub['subject_code']}", icon=":material/share:"):
#                 share_subject_dialog(sub['name'], sub['subject_code'])
#             st.space()

#         subject_card(
#             name = sub['name'],
#             code = sub['subject_code'],
#             section = sub['section'],
#             stats=stats,
#             footer_callback=share_btn
#         )
#     else:
#         st.info("NO SUBJECTS FOUND. CREATE ONE ABOVE")


# def teacher_tab_attendance_records():
#     st.header('Attendance Records')

#     teacher_id = st.session_state.teacher_data['teacher_id']

#     records = get_attendance_for_teacher(teacher_id)

#     if not records:
#         return
    
#     data = []

#     for r in records:
#         ts = r.get('timestamp')

#         data.append({
#             "ts_group": ts.split(".")[0] if ts else None,
#             "Time": datetime.fromisoformat(ts).strftime("%Y-%m-%d %I:%M %p") if ts else "N'A",
#             "Subject": r['subjects']['name'],
#             "Subject Code":r['subjects']['subject_code'],
#             "is_present": bool(r.get('is_present', False))
#         })


#     df = pd.DataFrame(data)



#     summary = (
#         df.groupby(['ts_group', 'Time', 'Subject', 'Subject Code'])
#         .agg(
#             Present_Count = ('is_present', 'sum'),
#             Total_Count =('is_present', 'count')
#         ).reset_index()

#     )

#     summary['Attendance Stats'] = (
#         "✅ " + summary['Present_Count'].astype(str) + " /"
#         + summary['Total_Count'].astype(str) + ' Students'
#     )

#     display_df = ( summary.sort_values(by='ts_group' ,ascending=False)
#                   [['Time', 'Subject', 'Subject Code', 'Attendance Stats']]
#                   )
    
#     st.dataframe(display_df, width='stretch', hide_index=True)


# def login_teacher(username, password):
#     if not username or not password:
#         return False
    
#     teacher = teacher_login(username, password)

#     if teacher:
#         st.session_state.user_role ='teacher'
#         st.session_state.teacher_data = teacher
#         st.session_state.is_logged_in = True
#         return True
    

#     return False
# def teacher_screen_login():
#     c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
#     with c1:
#         header_dashboard()
#     with c2:
#         if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
#             st.session_state['login_type'] = None
#             st.rerun()

#     st.header('Login using password', text_alignment='center')
#     st.space()
#     st.space()


#     teacher_username = st.text_input("Enter username", placeholder='ananyaroy')

#     teacher_pass = st.text_input("Enter password", type='password', placeholder="Enter password")

#     st.divider()

#     btnc1, btnc2 = st.columns(2)

#     with btnc1:
#         if st.button('Login', icon=':material/passkey:', shortcut='control+enter', width='stretch'):
#             if login_teacher(teacher_username, teacher_pass):
#                 st.toast("welcome back!", icon="👋")
#                 import time
#                 time.sleep(1)
#                 st.rerun()
#             else:
#                 st.error("Invalid username and password combo")

#     with btnc2:
#         if st.button('Register Instead', type="primary", icon=':material/passkey:', width='stretch'):
#             st.session_state.teacher_login_type = 'register'

#     footer_dashboard()



# def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
#     if not teacher_username or not teacher_name or not teacher_pass:
#         return False, "All Fields are required!"
#     if check_teacher_exists(teacher_username):
#         return False, "Username already taken"
#     if teacher_pass != teacher_pass_confirm:
#         return False, "Password doesn't match"
    
#     try:
#         create_teacher(teacher_username, teacher_pass, teacher_name)
#         return True, "Sucessfully Created! Login Now"
#     except Exception as e:
#         return False, "Unexpected Error!"
    

# def teacher_screen_register():
#     c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
#     with c1:
#         header_dashboard()
#     with c2:
#         if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
#             st.session_state['login_type'] = None
#             st.rerun()



#     st.header('Register your teacher profile')

#     st.space()
#     st.space()

    
#     teacher_username = st.text_input("Enter username", placeholder='ananyaroy')

#     teacher_name = st.text_input("Enter name", placeholder='Ananya Roy')

#     teacher_pass = st.text_input("Enter password", type='password', placeholder="Enter password")

#     teacher_pass_confirm = st.text_input("Confirm your password", type='password', placeholder="Enter password")

#     st.divider()

#     btnc1, btnc2 = st.columns(2)

#     with btnc1:
#         if st.button('Register now', icon=':material/passkey:', shortcut='control+enter', width='stretch'):
#             success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
#             if success:
#                 st.success(message)
#                 import time
#                 time.sleep(2)
#                 st.session_state.teacher_login_type = "login"
#                 st.rerun()
#             else:
#                 st.error(message)


#     with btnc2:
#         if st.button('Login Instead', type="primary", icon=':material/passkey:', width='stretch'):
#             st.session_state.teacher_login_type = 'login'

#     footer_dashboard()
import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.components.subject_card import subject_card
from src.database.db import check_teacher_exists, create_teacher, teacher_login, get_teacher_subjects, get_attendance_for_teacher
from src.components.dialog_create_subject import create_subject_dialog
from src.components.dialog_share_subject import share_subject_dialog
from src.components.dialog_add_photo import add_photos_dialog

from src.pipelines.face_pipeline import predict_attendance
from src.components.dialog_attendance_results import attendance_result_dialog
import numpy as np

from datetime import datetime

import pandas as pd

from src.database.config import supabase

from src.components.dialog_voice_attendance import voice_attendance_dialog

TEACHER_STYLES = """
<style>
@keyframes dashIn {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
}

.welcome-teacher {
    background: linear-gradient(135deg, #5865F2 0%, #7c3aed 60%, #EB459E 100%);
    border-radius: 20px;
    padding: 20px 24px;
    color: white;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0 8px 30px rgba(88,101,242,0.25);
    animation: dashIn 0.5s cubic-bezier(0.34,1.56,0.64,1) both;
}
.welcome-teacher .wt-icon {
    width: 48px; height: 48px;
    background: rgba(255,255,255,0.2);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.4rem;
    flex-shrink: 0;
}
.wt-name {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 1.05rem;
}
.wt-role {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.78rem;
    opacity: 0.7;
    margin-top: 2px;
}

.tab-section {
    background: white;
    border-radius: 20px;
    padding: 6px;
    display: flex;
    gap: 4px;
    box-shadow: 0 2px 12px rgba(88,101,242,0.08);
    border: 1px solid rgba(88,101,242,0.08);
    margin: 1rem 0;
}

.attendance-action-card {
    background: white;
    border-radius: 20px;
    padding: 24px;
    border: 1px solid rgba(88,101,242,0.1);
    box-shadow: 0 4px 20px rgba(88,101,242,0.07);
    margin-bottom: 1rem;
    animation: dashIn 0.4s ease both;
}

.photos-grid-header {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 1rem;
    color: #1a1a2e;
    margin: 1.5rem 0 0.75rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.photo-count-badge {
    background: linear-gradient(135deg, #5865F2, #EB459E);
    color: white;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 2px 9px;
    border-radius: 20px;
}

.stats-row {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin: 1rem 0;
}
.stat-card {
    flex: 1;
    min-width: 120px;
    background: white;
    border-radius: 16px;
    padding: 16px 20px;
    border: 1px solid rgba(88,101,242,0.1);
    box-shadow: 0 2px 12px rgba(88,101,242,0.06);
    text-align: center;
}
.stat-value {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 1.8rem;
    background: linear-gradient(135deg, #5865F2, #EB459E);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
    margin-bottom: 4px;
}
.stat-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.78rem;
    color: #9ca3c4;
    font-weight: 500;
}

.auth-card {
    background: white;
    border-radius: 28px;
    padding: 36px 32px;
    border: 1px solid rgba(88,101,242,0.1);
    box-shadow: 0 8px 40px rgba(88,101,242,0.08);
    margin: 1.5rem 0;
    animation: dashIn 0.5s ease both;
}
.auth-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 1.5rem;
    color: #1a1a2e;
    margin: 0 0 4px;
}
.auth-sub {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.88rem;
    color: #9ca3c4;
    margin: 0 0 1.5rem;
}

.empty-state {
    text-align: center;
    padding: 3rem 2rem;
    background: white;
    border-radius: 20px;
    border: 1px solid rgba(88,101,242,0.08);
    margin-top: 1rem;
}
.empty-icon { font-size: 3rem; margin-bottom: 12px; }
.empty-title {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    color: #1a1a2e;
    font-size: 1.05rem;
}
.empty-desc {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.85rem;
    color: #6b7280;
    margin-top: 4px;
}
</style>
"""


def teacher_screen():
    style_background_dashboard()
    style_base_layout()
    st.markdown(TEACHER_STYLES, unsafe_allow_html=True)

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()


def teacher_dashboard():
    teacher_data = st.session_state.teacher_data

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.markdown(f"""
            <div class="welcome-teacher">
                <div class="wt-icon">🎓</div>
                <div>
                    <div class="wt-name">{teacher_data['name']}</div>
                    <div class="wt-role">Teacher Dashboard</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.teacher_data
            st.rerun()

    st.space()

    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = 'take_attendance'

    tab1, tab2, tab3 = st.columns(3)
    with tab1:
        t1 = "primary" if st.session_state.current_teacher_tab == 'take_attendance' else "tertiary"
        if st.button('📸 Take Attendance', type=t1, width='stretch'):
            st.session_state.current_teacher_tab = 'take_attendance'
            st.rerun()
    with tab2:
        t2 = "primary" if st.session_state.current_teacher_tab == 'manage_subjects' else "tertiary"
        if st.button('📚 Subjects', type=t2, width='stretch'):
            st.session_state.current_teacher_tab = 'manage_subjects'
            st.rerun()
    with tab3:
        t3 = "primary" if st.session_state.current_teacher_tab == 'attendance_records' else "tertiary"
        if st.button('📊 Records', type=t3, width='stretch'):
            st.session_state.current_teacher_tab = 'attendance_records'
            st.rerun()

    st.divider()

    if st.session_state.current_teacher_tab == "take_attendance":
        teacher_tab_take_attendance()
    if st.session_state.current_teacher_tab == "manage_subjects":
        teacher_tab_manage_subjects()
    if st.session_state.current_teacher_tab == "attendance_records":
        teacher_tab_attendance_records()

    footer_dashboard()


def teacher_tab_take_attendance():
    teacher_id = st.session_state.teacher_data['teacher_id']

    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images = []

    subjects = get_teacher_subjects(teacher_id)

    if not subjects:
        st.markdown("""
            <div class="empty-state">
                <div class="empty-icon">📚</div>
                <div class="empty-title">No subjects created yet</div>
                <div class="empty-desc">Go to the Subjects tab to create your first subject</div>
            </div>
        """, unsafe_allow_html=True)
        return

    st.markdown("""
        <div style="font-family:'Syne',sans-serif; font-weight:700; font-size:1.3rem; color:#1a1a2e; margin-bottom:0.75rem">
            📸 Take AI Attendance
        </div>
    """, unsafe_allow_html=True)

    subject_options = {f"{s['name']} — {s['subject_code']}": s['subject_id'] for s in subjects}

    col1, col2 = st.columns([3, 1], vertical_alignment='bottom')
    with col1:
        selected_subject_label = st.selectbox('Select Subject', options=list(subject_options.keys()), label_visibility='collapsed')
    with col2:
        if st.button('+ Photos', type='primary', width='stretch'):
            add_photos_dialog()

    selected_subject_id = subject_options[selected_subject_label]

    st.divider()

    if st.session_state.attendance_images:
        count = len(st.session_state.attendance_images)
        st.markdown(f"""
            <div class="photos-grid-header">
                Added Photos <span class="photo-count-badge">{count}</span>
            </div>
        """, unsafe_allow_html=True)
        gallery_cols = st.columns(4)
        for idx, img in enumerate(st.session_state.attendance_images):
            with gallery_cols[idx % 4]:
                st.image(img, width='stretch', caption=f'Photo {idx + 1}')

    has_photos = bool(st.session_state.attendance_images)
    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button('🗑️ Clear Photos', width='stretch', type='tertiary', disabled=not has_photos):
            st.session_state.attendance_images = []
            st.rerun()

    with c2:
        if st.button('🤖 Run Face Analysis', width='stretch', type='secondary', disabled=not has_photos):
            with st.spinner('Deep scanning classroom photos…'):
                all_detected_ids = {}
                for idx, img in enumerate(st.session_state.attendance_images):
                    img_np = np.array(img.convert('RGB'))
                    detected, _, _ = predict_attendance(img_np)
                    if detected:
                        for sid in detected.keys():
                            student_id = int(sid)
                            all_detected_ids.setdefault(student_id, []).append(f"Photo {idx + 1}")

                enrolled_res = supabase.table('subject_students').select("*, students(*)").eq('subject_id', selected_subject_id).execute()
                enrolled_students = enrolled_res.data

                if not enrolled_students:
                    st.warning('No students enrolled in this course')
                else:
                    results, attendance_to_log = [], []
                    current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

                    for node in enrolled_students:
                        student = node['students']
                        sources = all_detected_ids.get(int(student['student_id']), [])
                        is_present = len(sources) > 0
                        results.append({
                            "Name": student['name'],
                            "ID": student['student_id'],
                            "Source": ", ".join(sources) if is_present else "-",
                            "Status": "✅ Present" if is_present else "❌ Absent"
                        })
                        attendance_to_log.append({
                            'student_id': student['student_id'],
                            'subject_id': selected_subject_id,
                            'timestamp': current_timestamp,
                            'is_present': bool(is_present)
                        })

                    attendance_result_dialog(pd.DataFrame(results), attendance_to_log)

    with c3:
        if st.button('🎙️ Voice Attendance', type='primary', width='stretch'):
            voice_attendance_dialog(selected_subject_id)


def teacher_tab_manage_subjects():
    teacher_id = st.session_state.teacher_data['teacher_id']

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div style="font-family:'Syne',sans-serif; font-weight:700; font-size:1.3rem; color:#1a1a2e">
                📚 Manage Subjects
            </div>
        """, unsafe_allow_html=True)
    with col2:
        if st.button('+ Create New Subject', width='stretch', type='primary'):
            create_subject_dialog(teacher_id)

    subjects = get_teacher_subjects(teacher_id)

    if subjects:
        # Quick stats
        total_students = sum(s.get('total_students', 0) for s in subjects)
        total_classes = sum(s.get('total_classes', 0) for s in subjects)
        st.markdown(f"""
            <div class="stats-row">
                <div class="stat-card">
                    <div class="stat-value">{len(subjects)}</div>
                    <div class="stat-label">Subjects</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">{total_students}</div>
                    <div class="stat-label">Total Students</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">{total_classes}</div>
                    <div class="stat-label">Classes Held</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        for sub in subjects:
            stats = [
                ("🫂", "Students", sub['total_students']),
                ("🕰️", "Classes", sub['total_classes']),
            ]

            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=stats,
            )
            if st.button(f"🔗 Share Code", key=f"share_{sub['subject_code']}", type='secondary'):
                share_subject_dialog(sub['name'], sub['subject_code'])
            st.space()
    else:
        st.markdown("""
            <div class="empty-state">
                <div class="empty-icon">📝</div>
                <div class="empty-title">No subjects yet</div>
                <div class="empty-desc">Click "Create New Subject" to get started</div>
            </div>
        """, unsafe_allow_html=True)


def teacher_tab_attendance_records():
    st.markdown("""
        <div style="font-family:'Syne',sans-serif; font-weight:700; font-size:1.3rem; color:#1a1a2e; margin-bottom:1rem">
            📊 Attendance Records
        </div>
    """, unsafe_allow_html=True)

    teacher_id = st.session_state.teacher_data['teacher_id']
    records = get_attendance_for_teacher(teacher_id)

    if not records:
        st.markdown("""
            <div class="empty-state">
                <div class="empty-icon">📋</div>
                <div class="empty-title">No records yet</div>
                <div class="empty-desc">Take attendance first to see records here</div>
            </div>
        """, unsafe_allow_html=True)
        return

    data = []
    for r in records:
        ts = r.get('timestamp')
        data.append({
            "ts_group": ts.split(".")[0] if ts else None,
            "Time": datetime.fromisoformat(ts).strftime("%Y-%m-%d %I:%M %p") if ts else "N/A",
            "Subject": r['subjects']['name'],
            "Subject Code": r['subjects']['subject_code'],
            "is_present": bool(r.get('is_present', False))
        })

    df = pd.DataFrame(data)
    summary = (
        df.groupby(['ts_group', 'Time', 'Subject', 'Subject Code'])
        .agg(Present_Count=('is_present', 'sum'), Total_Count=('is_present', 'count'))
        .reset_index()
    )
    summary['Attendance'] = "✅ " + summary['Present_Count'].astype(str) + " / " + summary['Total_Count'].astype(str) + " students"
    display_df = summary.sort_values(by='ts_group', ascending=False)[['Time', 'Subject', 'Subject Code', 'Attendance']]
    st.dataframe(display_df, width='stretch', hide_index=True)


def login_teacher(username, password):
    if not username or not password:
        return False
    teacher = teacher_login(username, password)
    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
    return False


def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("← Back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.markdown("""
        <div class="auth-card">
            <div class="auth-title">🎓 Teacher Login</div>
            <div class="auth-sub">Sign in to manage your classes</div>
        </div>
    """, unsafe_allow_html=True)

    with st.container(border=True):
        teacher_username = st.text_input("Username", placeholder='e.g. ananya_roy')
        teacher_pass = st.text_input("Password", type='password', placeholder='Enter your password')

        st.divider()

        btnc1, btnc2 = st.columns(2)
        with btnc1:
            if st.button('🔐 Login', shortcut='control+enter', width='stretch', type='primary'):
                if login_teacher(teacher_username, teacher_pass):
                    st.toast("Welcome back! 👋")
                    import time
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Invalid username or password")

        with btnc2:
            if st.button('New here? Register →', type='secondary', width='stretch'):
                st.session_state.teacher_login_type = 'register'
                st.rerun()

    footer_dashboard()


def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All fields are required"
    if check_teacher_exists(teacher_username):
        return False, "Username already taken"
    if teacher_pass != teacher_pass_confirm:
        return False, "Passwords don't match"
    try:
        create_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Account created! Please login."
    except Exception:
        return False, "Unexpected error — please try again"


def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("← Back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.markdown("""
        <div class="auth-card">
            <div class="auth-title">✨ Create Account</div>
            <div class="auth-sub">Set up your teacher profile on AI RollCall</div>
        </div>
    """, unsafe_allow_html=True)

    with st.container(border=True):
        teacher_username = st.text_input("Username", placeholder='e.g. ananya_roy')
        teacher_name = st.text_input("Full Name", placeholder='e.g. Ananya Roy')
        teacher_pass = st.text_input("Password", type='password', placeholder='Choose a strong password')
        teacher_pass_confirm = st.text_input("Confirm Password", type='password', placeholder='Repeat password')

        st.divider()

        btnc1, btnc2 = st.columns(2)
        with btnc1:
            if st.button('🚀 Register Now', shortcut='control+enter', width='stretch', type='primary'):
                success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
                if success:
                    st.success(message)
                    import time
                    time.sleep(2)
                    st.session_state.teacher_login_type = "login"
                    st.rerun()
                else:
                    st.error(message)

        with btnc2:
            if st.button('Already have account? Login →', type='secondary', width='stretch'):
                st.session_state.teacher_login_type = 'login'
                st.rerun()

    footer_dashboard()