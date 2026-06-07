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
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
    header_home()
    style_background_home()
    style_base_layout()

    st.markdown("""
        <style>
        @keyframes portalCardIn {
            from { opacity: 0; transform: translateY(30px) scale(0.96); }
            to   { opacity: 1; transform: translateY(0) scale(1); }
        }

        .portal-label {
            font-family: 'DM Sans', sans-serif;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: rgba(255,255,255,0.5);
            margin-bottom: 6px;
        }

        .portal-title {
            font-family: 'Syne', sans-serif !important;
            font-weight: 800 !important;
            font-size: 1.6rem !important;
            color: white !important;
            margin: 0 0 4px 0 !important;
            line-height: 1.1 !important;
        }

        .portal-desc {
            font-family: 'DM Sans', sans-serif;
            font-size: 0.85rem;
            color: rgba(255,255,255,0.55);
            margin: 0 0 1.2rem 0;
        }

        /* override column styles for the portal cards */
        .stApp div[data-testid="stColumn"]:nth-child(1) {
            animation: portalCardIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.2s both;
        }
        .stApp div[data-testid="stColumn"]:nth-child(2) {
            animation: portalCardIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.35s both;
        }

        .mascot-wrap {
            display: flex;
            justify-content: center;
            margin: 0.5rem 0 1.2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown('<div class="portal-label">for learners</div>', unsafe_allow_html=True)
        st.markdown('<div class="portal-title">Student<br/>Portal</div>', unsafe_allow_html=True)
        st.markdown('<div class="portal-desc">Log attendance with your face or voice</div>', unsafe_allow_html=True)
        st.markdown('<div class="mascot-wrap">', unsafe_allow_html=True)
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=110)
        st.markdown('</div>', unsafe_allow_html=True)
        if st.button('Enter Student Portal →', type='primary', key='student_btn'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.markdown('<div class="portal-label">for educators</div>', unsafe_allow_html=True)
        st.markdown('<div class="portal-title">Teacher<br/>Portal</div>', unsafe_allow_html=True)
        st.markdown('<div class="portal-desc">Take AI-powered classroom attendance</div>', unsafe_allow_html=True)
        st.markdown('<div class="mascot-wrap">', unsafe_allow_html=True)
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=125)
        st.markdown('</div>', unsafe_allow_html=True)
        if st.button('Enter Teacher Portal →', type='primary', key='teacher_btn'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    footer_home()