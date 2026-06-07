# # import streamlit as st



# # def style_background_home():

# #     st.markdown("""
# #         <style>

# #                 .stApp {
# #                     background: #5865F2 !important;
# #                 }

# #                 .stApp div[data-testid="stColumn"]{
# #                     background-color:#E0E3FF !important;
# #                     padding:2.5rem !important;
# #                     border-radius: 5rem !important;
# #                     }
# #         </style>  

# #                 """
# #             ,unsafe_allow_html=True)
    

# # def style_background_dashboard():

# #     st.markdown("""
# #         <style>

# #                 .stApp {
# #                     background: #E0E3FF !important;
# #                 }

# #         </style>  

# #                 """
# #             ,unsafe_allow_html=True)
    

    

# # def style_base_layout():
# # # asdasd
# #     st.markdown("""
# #         <style>
# #         @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
# #         @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
# #          /* Hide Top Bar of streamlit */
                
# #             #MainMenu, footer, header {
# #                 visibility: hidden;
# #             }
                
# #             .block-container {
# #                 padding-top:1.5rem !important;    
# #             }

# #             h1 {
# #                 font-family: 'Climate Crisis', sans-serif !important;
# #                 font-size: 3.5rem !important;
# #                 line-height:1.1 1important;
# #                 margin-bottom:0rem !important;
# #             }
                

# #             h2 {
# #                 font-family: 'Climate Crisis', sans-serif !important;
# #                 font-size: 2rem !important;
# #                 line-height:0.9 !important;
# #                 margin-bottom:0rem !important;
# #             }
                
# #             h3, h4, p {
# #                 font-family: 'Outfit', sans-serif;    
# #             }
                

# #             button{
# #                 border-radius: 1.5rem !important;
# #                 background-color: #5865F2 !important;
# #                 color: white !important;
# #                 padding: 10px 20px !important;
# #                 border: none !important;
# #                 transition: transform 0.25s ease-in-out !important;
# #                 }

# #             button[kind="secondary"]{
# #                 border-radius: 1.5rem !important;
# #                 background-color: #EB459E !important;
# #                 color: white !important;
# #                 padding: 10px 20px !important;
# #                 border: none !important;
# #                 transition: transform 0.25s ease-in-out !important;
# #                 }

# #             button[kind="tertiary"]{
# #                 border-radius: 1.5rem !important;
# #                 background-color: black !important;
# #                 color: white !important;
# #                 padding: 10px 20px !important;
# #                 border: none !important;
# #                 transition: transform 0.25s ease-in-out !important;
# #                 }

# #             button:hover{
# #                 transform :scale(1.05)}
# #         </style>  

# #                 """
# #             ,unsafe_allow_html=True)
# import streamlit as st



# def style_background_home():
#     st.markdown("""
#         <style>
#         .stApp {
#             background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%) !important;
#             min-height: 100vh;
#         }

#         .stApp::before {
#             content: '';
#             position: fixed;
#             top: -50%;
#             left: -50%;
#             width: 200%;
#             height: 200%;
#             background: radial-gradient(ellipse at 20% 50%, rgba(88, 101, 242, 0.3) 0%, transparent 50%),
#                         radial-gradient(ellipse at 80% 20%, rgba(235, 69, 158, 0.2) 0%, transparent 50%),
#                         radial-gradient(ellipse at 60% 80%, rgba(139, 92, 246, 0.2) 0%, transparent 50%);
#             animation: bgPulse 8s ease-in-out infinite alternate;
#             pointer-events: none;
#             z-index: 0;
#         }

#         @keyframes bgPulse {
#             0% { transform: scale(1) rotate(0deg); }
#             100% { transform: scale(1.1) rotate(3deg); }
#         }

#         .stApp div[data-testid="stColumn"] {
#             background: rgba(255, 255, 255, 0.07) !important;
#             backdrop-filter: blur(20px) !important;
#             -webkit-backdrop-filter: blur(20px) !important;
#             padding: 2.5rem !important;
#             border-radius: 2rem !important;
#             border: 1px solid rgba(255, 255, 255, 0.15) !important;
#             box-shadow: 0 25px 50px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.1) !important;
#             transition: transform 0.3s ease, box-shadow 0.3s ease !important;
#             animation: cardFloat 0.6s ease-out both;
#         }

#         .stApp div[data-testid="stColumn"]:hover {
#             transform: translateY(-4px) !important;
#             box-shadow: 0 35px 70px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.15) !important;
#         }

#         @keyframes cardFloat {
#             from { opacity: 0; transform: translateY(30px); }
#             to { opacity: 1; transform: translateY(0); }
#         }
#         </style>
#     """, unsafe_allow_html=True)


# def style_background_dashboard():
#     st.markdown("""
#         <style>
#         .stApp {
#             background: linear-gradient(160deg, #f0f2ff 0%, #e8ebff 40%, #f5f0ff 100%) !important;
#             min-height: 100vh;
#         }

#         .stApp::before {
#             content: '';
#             position: fixed;
#             top: 0; left: 0;
#             width: 100%; height: 100%;
#             background: 
#                 radial-gradient(ellipse at 10% 10%, rgba(88, 101, 242, 0.08) 0%, transparent 50%),
#                 radial-gradient(ellipse at 90% 90%, rgba(235, 69, 158, 0.06) 0%, transparent 50%);
#             pointer-events: none;
#             z-index: 0;
#         }
#         </style>
#     """, unsafe_allow_html=True)


# def style_base_layout():
#     st.markdown("""
#         <style>
#         @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap');

#         /* ── RESET ── */
#         #MainMenu, footer, header { visibility: hidden; }

#         .block-container {
#             padding-top: 1.5rem !important;
#             position: relative;
#             z-index: 1;
#         }

#         /* ── TYPOGRAPHY ── */
#         h1 {
#             font-family: 'Syne', sans-serif !important;
#             font-weight: 800 !important;
#             font-size: 3.2rem !important;
#             line-height: 1.05 !important;
#             letter-spacing: -0.03em !important;
#             background: linear-gradient(135deg, #5865F2, #EB459E) !important;
#             -webkit-background-clip: text !important;
#             -webkit-text-fill-color: transparent !important;
#             background-clip: text !important;
#             margin-bottom: 0 !important;
#         }

#         h2 {
#             font-family: 'Syne', sans-serif !important;
#             font-weight: 700 !important;
#             font-size: 1.9rem !important;
#             line-height: 1 !important;
#             letter-spacing: -0.02em !important;
#             color: #1a1a2e !important;
#             margin-bottom: 0 !important;
#         }

#         h3, h4 {
#             font-family: 'Syne', sans-serif !important;
#             font-weight: 600 !important;
#             color: #2d2d44 !important;
#         }

#         p, label, span, div {
#             font-family: 'DM Sans', sans-serif !important;
#         }

#         /* ── BUTTONS ── */
#         button {
#             font-family: 'DM Sans', sans-serif !important;
#             font-weight: 600 !important;
#             border-radius: 50px !important;
#             background: linear-gradient(135deg, #5865F2, #7c3aed) !important;
#             color: white !important;
#             border: none !important;
#             transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
#             letter-spacing: 0.01em !important;
#             position: relative !important;
#             overflow: hidden !important;
#         }

#         button::after {
#             content: '';
#             position: absolute;
#             top: 0; left: -100%;
#             width: 100%; height: 100%;
#             background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent);
#             transition: left 0.4s ease;
#         }

#         button:hover::after { left: 100%; }

#         button:hover {
#             transform: translateY(-2px) scale(1.02) !important;
#             box-shadow: 0 8px 25px rgba(88, 101, 242, 0.4) !important;
#         }

#         button:active {
#             transform: translateY(0) scale(0.98) !important;
#         }

#         button[kind="secondary"] {
#             background: linear-gradient(135deg, #EB459E, #f72585) !important;
#             box-shadow: 0 4px 15px rgba(235, 69, 158, 0.2) !important;
#         }

#         button[kind="secondary"]:hover {
#             box-shadow: 0 8px 25px rgba(235, 69, 158, 0.45) !important;
#         }

#         button[kind="tertiary"] {
#             background: linear-gradient(135deg, #1a1a2e, #2d2d44) !important;
#             box-shadow: 0 4px 15px rgba(0,0,0,0.15) !important;
#         }

#         button[kind="tertiary"]:hover {
#             box-shadow: 0 8px 25px rgba(0,0,0,0.3) !important;
#         }

#         /* ── INPUTS ── */
#         input, textarea {
#             font-family: 'DM Sans', sans-serif !important;
#             border-radius: 16px !important;
#             border: 2px solid rgba(88, 101, 242, 0.15) !important;
#             transition: all 0.2s ease !important;
#             background: rgba(255,255,255,0.8) !important;
#         }

#         input:focus, textarea:focus {
#             border-color: #5865F2 !important;
#             box-shadow: 0 0 0 4px rgba(88, 101, 242, 0.1) !important;
#         }

#         /* ── SELECT BOX ── */
#         .stSelectbox > div > div {
#             border-radius: 16px !important;
#             border: 2px solid rgba(88, 101, 242, 0.15) !important;
#             background: rgba(255,255,255,0.8) !important;
#         }

#         /* ── DIVIDER ── */
#         hr {
#             border: none !important;
#             height: 1px !important;
#             background: linear-gradient(90deg, transparent, rgba(88, 101, 242, 0.2), transparent) !important;
#             margin: 1.5rem 0 !important;
#         }

#         /* ── SPINNER ── */
#         .stSpinner > div {
#             border-color: #5865F2 transparent transparent transparent !important;
#         }

#         /* ── TOAST ── */
#         .stToast {
#             border-radius: 16px !important;
#             backdrop-filter: blur(10px) !important;
#         }

#         /* ── DATAFRAME ── */
#         .stDataFrame {
#             border-radius: 16px !important;
#             overflow: hidden !important;
#             box-shadow: 0 4px 20px rgba(88, 101, 242, 0.1) !important;
#         }

#         /* ── DIALOG ── */
#         div[role="dialog"] {
#             border-radius: 24px !important;
#             border: 1px solid rgba(88, 101, 242, 0.15) !important;
#             box-shadow: 0 30px 60px rgba(0,0,0,0.2) !important;
#         }

#         /* ── FADE IN ANIMATION ── */
#         @keyframes fadeInUp {
#             from { opacity: 0; transform: translateY(20px); }
#             to   { opacity: 1; transform: translateY(0); }
#         }

#         .element-container {
#             animation: fadeInUp 0.4s ease-out both;
#         }

#         /* ── CAMERA ── */
#         .stCameraInput > div {
#             border-radius: 20px !important;
#             overflow: hidden !important;
#             border: 2px solid rgba(88, 101, 242, 0.2) !important;
#         }

#         /* ── FILE UPLOADER ── */
#         .stFileUploader > div {
#             border-radius: 20px !important;
#             border: 2px dashed rgba(88, 101, 242, 0.3) !important;
#         }

#         /* ── CONTAINER ── */
#         div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] {
#             animation: fadeInUp 0.5s ease-out both;
#         }

#         /* ── SCROLLBAR ── */
#         ::-webkit-scrollbar { width: 6px; }
#         ::-webkit-scrollbar-track { background: transparent; }
#         ::-webkit-scrollbar-thumb { 
#             background: linear-gradient(#5865F2, #EB459E);
#             border-radius: 3px;
#         }
#         </style>
#     """, unsafe_allow_html=True)
import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
        .stApp {
            background: #080810 !important;
            min-height: 100vh;
        }

        .stApp::before {
            content: '';
            position: fixed;
            inset: 0;
            background:
                radial-gradient(ellipse 55% 50% at 8% 12%,  rgba(255, 50, 110, 0.32) 0%, transparent 55%),
                radial-gradient(ellipse 50% 45% at 92% 10%,  rgba(30, 170, 255, 0.26) 0%, transparent 55%),
                radial-gradient(ellipse 40% 40% at 50% 92%,  rgba(100, 255, 180, 0.18) 0%, transparent 55%),
                radial-gradient(ellipse 35% 35% at 85% 80%,  rgba(255, 190, 50, 0.18) 0%, transparent 55%),
                radial-gradient(ellipse 30% 30% at 20% 75%,  rgba(160, 80, 255, 0.16) 0%, transparent 55%);
            pointer-events: none;
            z-index: 0;
            animation: ambientPulse 10s ease-in-out infinite alternate;
        }

        @keyframes ambientPulse {
            0%   { opacity: 0.8; transform: scale(1); }
            100% { opacity: 1;   transform: scale(1.04); }
        }

        .stApp div[data-testid="stColumn"] {
            background: transparent !important;
            backdrop-filter: none !important;
            -webkit-backdrop-filter: none !important;
            padding: 0 4px !important;
            border-radius: 0 !important;
            border: none !important;
            box-shadow: none !important;
            animation: none !important;
        }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(160deg, #f0f2ff 0%, #e8ebff 40%, #f5f0ff 100%) !important;
            min-height: 100vh;
        }
        .stApp::before {
            content: '';
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background:
                radial-gradient(ellipse at 10% 10%, rgba(88, 101, 242, 0.08) 0%, transparent 50%),
                radial-gradient(ellipse at 90% 90%, rgba(235, 69, 158, 0.06) 0%, transparent 50%);
            pointer-events: none;
            z-index: 0;
        }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800;900&family=DM+Sans:wght@300;400;500;600&display=swap');

        #MainMenu, footer, header { visibility: hidden; }

        .block-container {
            padding-top: 1.5rem !important;
            position: relative;
            z-index: 1;
        }

        h1 {
            font-family: 'Syne', sans-serif !important;
            font-weight: 800 !important;
            font-size: 3.2rem !important;
            line-height: 1.05 !important;
            letter-spacing: -0.03em !important;
            background: linear-gradient(135deg, #ff3c78, #a855f7, #1ab8ff) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
            margin-bottom: 0 !important;
        }
        h2 {
            font-family: 'Syne', sans-serif !important;
            font-weight: 700 !important;
            font-size: 1.9rem !important;
            line-height: 1 !important;
            letter-spacing: -0.02em !important;
            color: #1a1a2e !important;
            margin-bottom: 0 !important;
        }
        h3, h4 {
            font-family: 'Syne', sans-serif !important;
            font-weight: 600 !important;
            color: #2d2d44 !important;
        }
        p, label, span, div {
            font-family: 'DM Sans', sans-serif !important;
        }

        .stTextInput label,
        .stSelectbox label,
        .stFileUploader label,
        .stCameraInput label,
        .stAudioInput label,
        .stRadio label,
        .stCheckbox label,
        div[data-testid="stWidgetLabel"] p,
        div[data-testid="stWidgetLabel"] label {
            color: #1a1a2e !important;
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.88rem !important;
            -webkit-text-fill-color: #1a1a2e !important;
        }

        input, textarea {
            font-family: 'DM Sans', sans-serif !important;
            font-size: 0.95rem !important;
            color: #1a1a2e !important;
            -webkit-text-fill-color: #1a1a2e !important;
            border-radius: 14px !important;
            border: 2px solid rgba(88, 101, 242, 0.2) !important;
            background: #ffffff !important;
            transition: all 0.2s ease !important;
        }
        input::placeholder, textarea::placeholder {
            color: #9ca3af !important;
            -webkit-text-fill-color: #9ca3af !important;
            opacity: 1 !important;
        }
        input:focus, textarea:focus {
            border-color: #a855f7 !important;
            box-shadow: 0 0 0 3px rgba(168, 85, 247, 0.12) !important;
            background: #ffffff !important;
            color: #1a1a2e !important;
            -webkit-text-fill-color: #1a1a2e !important;
        }
        .stTextInput > div > div,
        .stTextInput > div > div > div {
            background: #ffffff !important;
            border-radius: 14px !important;
        }

        .stSelectbox > div > div {
            border-radius: 14px !important;
            border: 2px solid rgba(88, 101, 242, 0.2) !important;
            background: #ffffff !important;
            color: #1a1a2e !important;
        }
        .stSelectbox > div > div > div {
            color: #1a1a2e !important;
            -webkit-text-fill-color: #1a1a2e !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: #ffffff !important;
            border-radius: 20px !important;
            border: 1px solid rgba(88, 101, 242, 0.12) !important;
            box-shadow: 0 4px 20px rgba(88, 101, 242, 0.07) !important;
            padding: 1.2rem !important;
        }

        button {
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 600 !important;
            border-radius: 50px !important;
            background: linear-gradient(135deg, #ff3c78, #a855f7) !important;
            color: white !important;
            -webkit-text-fill-color: white !important;
            border: none !important;
            transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        }
        button:hover {
            transform: translateY(-2px) scale(1.02) !important;
            box-shadow: 0 8px 24px rgba(168, 85, 247, 0.4) !important;
        }
        button:active {
            transform: translateY(0) scale(0.98) !important;
        }
        button[kind="secondary"] {
            background: linear-gradient(135deg, #1ab8ff, #00e0a0) !important;
            color: white !important;
            -webkit-text-fill-color: white !important;
        }
        button[kind="secondary"]:hover {
            box-shadow: 0 8px 24px rgba(26, 184, 255, 0.4) !important;
        }
        button[kind="tertiary"] {
            background: rgba(255,255,255,0.08) !important;
            color: #1a1a2e !important;
            -webkit-text-fill-color: #1a1a2e !important;
            border: 1px solid rgba(88, 101, 242, 0.18) !important;
        }

        hr {
            border: none !important;
            height: 1px !important;
            background: linear-gradient(90deg, transparent, rgba(168,85,247,0.2), transparent) !important;
            margin: 1.5rem 0 !important;
        }

        .stDataFrame {
            border-radius: 16px !important;
            overflow: hidden !important;
            box-shadow: 0 4px 20px rgba(88, 101, 242, 0.1) !important;
        }

        div[role="dialog"] {
            border-radius: 24px !important;
            border: 1px solid rgba(88, 101, 242, 0.12) !important;
            box-shadow: 0 30px 60px rgba(0,0,0,0.18) !important;
            background: #ffffff !important;
        }
        div[role="dialog"] p,
        div[role="dialog"] label {
            color: #1a1a2e !important;
            -webkit-text-fill-color: #1a1a2e !important;
        }
        div[role="dialog"] button,
        div[role="dialog"] button span {
            color: white !important;
            -webkit-text-fill-color: white !important;
        }

        .stAlert p {
            color: inherit !important;
            -webkit-text-fill-color: inherit !important;
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(16px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .element-container {
            animation: fadeInUp 0.35s ease-out both;
        }

        .stCameraInput > div {
            border-radius: 20px !important;
            overflow: hidden !important;
            border: 2px solid rgba(168, 85, 247, 0.2) !important;
        }
        .stFileUploader > div {
            border-radius: 20px !important;
            border: 2px dashed rgba(168, 85, 247, 0.25) !important;
            background: #fafbff !important;
        }

        ::-webkit-scrollbar { width: 5px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(#ff3c78, #1ab8ff);
            border-radius: 3px;
        }
        </style>
    """, unsafe_allow_html=True)
