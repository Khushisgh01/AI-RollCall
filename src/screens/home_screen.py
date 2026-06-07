# import streamlit as st
# from src.components.header import header_home
# from src.components.footer import footer_home
# from src.ui.base_layout import style_base_layout, style_background_home
# def home_screen():


#     header_home()
#     style_background_home()
#     style_base_layout()


#     col1, col2 = st.columns(2, gap="large")

#     with col1:
#         st.header("I'm Student")
#         st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
#         if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
#             st.session_state['login_type']='student'
#             st.rerun()

#     with col2:
#         st.header("I'm Teacher")
#         st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
#         if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
#             st.session_state['login_type']='teacher'
#             st.rerun()

#     footer_home()
import streamlit as st
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
    style_background_home()
    style_base_layout()

    from src.components.header import header_home
    header_home()

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@800;900&family=DM+Sans:wght@400;600;700&display=swap');

        @keyframes cardSlideUp {
            from { opacity: 0; transform: translateY(36px) scale(0.95); }
            to   { opacity: 1; transform: translateY(0) scale(1); }
        }

        .portals-row {
            display: flex;
            gap: 14px;
            margin: 1.4rem 0 0.5rem;
            width: 100%;
        }

        .portal-card {
            flex: 1;
            border-radius: 26px;
            padding: 26px 20px 22px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        /* Top-light shimmer */
        .portal-card::after {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: 26px;
            background: radial-gradient(ellipse 80% 40% at 50% 0%,
                rgba(255,255,255,0.09) 0%, transparent 65%);
            pointer-events: none;
        }

        .student-card {
            background: linear-gradient(145deg,
                rgba(255, 45, 110, 0.22) 0%,
                rgba(160, 60, 255, 0.22) 60%,
                rgba(255, 45, 110, 0.08) 100%);
            border: 1px solid rgba(255, 80, 140, 0.28);
            box-shadow:
                0 20px 50px rgba(255, 45, 110, 0.2),
                0 0 0 0.5px rgba(255,255,255,0.05) inset;
            animation: cardSlideUp 0.65s cubic-bezier(0.34,1.56,0.64,1) 0.35s both;
        }

        .teacher-card {
            background: linear-gradient(145deg,
                rgba(26, 184, 255, 0.22) 0%,
                rgba(0, 224, 160, 0.18) 60%,
                rgba(26, 184, 255, 0.08) 100%);
            border: 1px solid rgba(50, 200, 255, 0.28);
            box-shadow:
                0 20px 50px rgba(26, 184, 255, 0.2),
                0 0 0 0.5px rgba(255,255,255,0.05) inset;
            animation: cardSlideUp 0.65s cubic-bezier(0.34,1.56,0.64,1) 0.5s both;
        }

        .card-emoji {
            font-size: 2.8rem;
            margin-bottom: 10px;
            display: block;
            filter: drop-shadow(0 4px 10px rgba(0,0,0,0.4));
        }

        .card-role-label {
            font-family: 'DM Sans', sans-serif;
            font-size: 0.63rem;
            font-weight: 600;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            margin-bottom: 5px;
        }
        .student-card .card-role-label {
            color: rgba(255, 180, 210, 0.65);
            -webkit-text-fill-color: rgba(255, 180, 210, 0.65);
        }
        .teacher-card .card-role-label {
            color: rgba(120, 230, 255, 0.65);
            -webkit-text-fill-color: rgba(120, 230, 255, 0.65);
        }

        .card-title {
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 1.4rem;
            line-height: 1.1;
            color: #ffffff;
            -webkit-text-fill-color: #ffffff;
            margin-bottom: 8px;
        }

        .card-desc {
            font-family: 'DM Sans', sans-serif;
            font-size: 0.74rem;
            line-height: 1.55;
            margin-bottom: 18px;
        }
        .student-card .card-desc {
            color: rgba(255, 210, 225, 0.58);
            -webkit-text-fill-color: rgba(255, 210, 225, 0.58);
        }
        .teacher-card .card-desc {
            color: rgba(160, 235, 255, 0.58);
            -webkit-text-fill-color: rgba(160, 235, 255, 0.58);
        }

        .card-cta {
            display: inline-block;
            padding: 9px 22px;
            border-radius: 50px;
            font-family: 'DM Sans', sans-serif;
            font-weight: 700;
            font-size: 0.8rem;
            letter-spacing: 0.02em;
            color: white !important;
            -webkit-text-fill-color: white !important;
        }
        .student-card .card-cta {
            background: linear-gradient(135deg, #ff3c78, #b040e8);
            box-shadow: 0 4px 18px rgba(255, 60, 120, 0.5);
        }
        .teacher-card .card-cta {
            background: linear-gradient(135deg, #1ab8ff, #00e0a0);
            box-shadow: 0 4px 18px rgba(26, 184, 255, 0.45);
        }
        </style>

        <div class="portals-row">
            <div class="portal-card student-card">
                <span class="card-emoji">🎓</span>
                <div class="card-role-label">For Learners</div>
                <div class="card-title">Student<br/>Portal</div>
                <div class="card-desc">Log attendance via face recognition or voice ID</div>
                <div class="card-cta">Enter Portal →</div>
            </div>
            <div class="portal-card teacher-card">
                <span class="card-emoji">📋</span>
                <div class="card-role-label">For Educators</div>
                <div class="card-title">Teacher<br/>Portal</div>
                <div class="card-desc">Take AI-powered classroom attendance in seconds</div>
                <div class="card-cta">Enter Portal →</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="small")
    with col1:
        if st.button('🎓 Student Portal', type='primary', key='student_btn', width='stretch'):
            st.session_state['login_type'] = 'student'
            st.rerun()
    with col2:
        if st.button('📋 Teacher Portal', type='primary', key='teacher_btn', width='stretch'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    footer_home()
