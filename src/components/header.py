# # # import streamlit as st


# # # def header_home():

# # #     logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
# # #     st.markdown(f"""
# # #         <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
# # #             <img src='{logo_url}' style='height:100px;' />
# # #             <h1 style='text-align:center; color:#E0E3FF'>SNAP<br/>CLASS</h1>
# # #         </div>   
                
# # #                 """, unsafe_allow_html=True)


# # # def header_dashboard():

# # #     logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
# # #     st.markdown(f"""
# # #         <div style="display:flex; align-items:center; justify-content:center; gap:10px">
# # #             <img src='{logo_url}' style='height:85px;' />
# # #             <h2 style='text-align:left; color:#5865F2'>SNAP<br/>CLASS</h1>
# # #         </div>   
                
# # #                 """, unsafe_allow_html=True)

# # import streamlit as st


# # def header_home():
# #     logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

# #     st.markdown(f"""
# #         <style>
# #         @keyframes logoEntrance {{
# #             0%   {{ opacity: 0; transform: scale(0.5) rotate(-10deg); }}
# #             60%  {{ transform: scale(1.1) rotate(2deg); }}
# #             100% {{ opacity: 1; transform: scale(1) rotate(0deg); }}
# #         }}
# #         @keyframes titleReveal {{
# #             from {{ opacity: 0; letter-spacing: 0.5em; }}
# #             to   {{ opacity: 1; letter-spacing: -0.03em; }}
# #         }}
# #         @keyframes taglineSlide {{
# #             from {{ opacity: 0; transform: translateY(10px); }}
# #             to   {{ opacity: 1; transform: translateY(0); }}
# #         }}
# #         @keyframes glowPulse {{
# #             0%, 100% {{ filter: drop-shadow(0 0 15px rgba(88,101,242,0.4)); }}
# #             50%       {{ filter: drop-shadow(0 0 30px rgba(235,69,158,0.5)); }}
# #         }}
# #         @keyframes badgePop {{
# #             from {{ opacity: 0; transform: scale(0); }}
# #             to   {{ opacity: 1; transform: scale(1); }}
# #         }}

# #         .hero-wrapper {{
# #             display: flex;
# #             flex-direction: column;
# #             align-items: center;
# #             justify-content: center;
# #             padding: 3rem 1rem 2rem;
# #             text-align: center;
# #             position: relative;
# #         }}

# #         .logo-ring {{
# #             position: relative;
# #             display: inline-block;
# #             animation: logoEntrance 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) both;
# #         }}

# #         .logo-ring::before {{
# #             content: '';
# #             position: absolute;
# #             inset: -12px;
# #             border-radius: 50%;
# #             background: conic-gradient(from 0deg, #5865F2, #EB459E, #5865F2);
# #             animation: glowPulse 3s ease-in-out infinite;
# #             z-index: 0;
# #             border-radius: 50%;
# #             padding: 3px;
# #             -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - 3px), black 0);
# #         }}

# #         .logo-img {{
# #             height: 100px;
# #             position: relative;
# #             z-index: 1;
# #             border-radius: 50%;
# #         }}

# #         .hero-title {{
# #             font-family: 'Syne', sans-serif !important;
# #             font-weight: 900 !important;
# #             font-size: 4rem !important;
# #             line-height: 0.95 !important;
# #             background: linear-gradient(135deg, #ffffff 0%, #c4c8ff 50%, #ff9dd5 100%);
# #             -webkit-background-clip: text;
# #             -webkit-text-fill-color: transparent;
# #             background-clip: text;
# #             margin: 1rem 0 0.25rem !important;
# #             animation: titleReveal 0.7s cubic-bezier(0.16, 1, 0.3, 1) 0.3s both;
# #             letter-spacing: -0.03em;
# #         }}

# #         .hero-tagline {{
# #             font-family: 'DM Sans', sans-serif;
# #             font-size: 0.95rem;
# #             color: rgba(255,255,255,0.6);
# #             letter-spacing: 0.08em;
# #             text-transform: uppercase;
# #             animation: taglineSlide 0.6s ease 0.6s both;
# #             margin-bottom: 0.5rem;
# #         }}

# #         .creator-badge {{
# #             display: inline-flex;
# #             align-items: center;
# #             gap: 6px;
# #             background: rgba(255,255,255,0.08);
# #             border: 1px solid rgba(255,255,255,0.15);
# #             backdrop-filter: blur(10px);
# #             padding: 6px 16px;
# #             border-radius: 50px;
# #             font-family: 'DM Sans', sans-serif;
# #             font-size: 0.8rem;
# #             color: rgba(255,255,255,0.7);
# #             margin-top: 0.75rem;
# #             animation: badgePop 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) 0.9s both;
# #         }}

# #         .creator-badge span {{
# #             background: linear-gradient(135deg, #c4c8ff, #ff9dd5);
# #             -webkit-background-clip: text;
# #             -webkit-text-fill-color: transparent;
# #             background-clip: text;
# #             font-weight: 600;
# #         }}
# #         </style>

# #         <div class="hero-wrapper">
# #             <div class="logo-ring">
# #                 <img src='{logo_url}' class='logo-img' />
# #             </div>
# #             <h1 class='hero-title'>AI<br/>RollCall</h1>
# #             <p class='hero-tagline'>AI-Powered Attendance</p>
# #             <div class='creator-badge'>✦ crafted by <span>Khushi</span></div>
# #         </div>
# #     """, unsafe_allow_html=True)


# # def header_dashboard():
# #     logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

# #     st.markdown(f"""
# #         <style>
# #         @keyframes dashLogoIn {{
# #             from {{ opacity: 0; transform: scale(0.7) rotate(-5deg); }}
# #             to   {{ opacity: 1; transform: scale(1) rotate(0deg); }}
# #         }}
# #         @keyframes dashTitleIn {{
# #             from {{ opacity: 0; transform: translateX(-15px); }}
# #             to   {{ opacity: 1; transform: translateX(0); }}
# #         }}

# #         .dash-header {{
# #             display: flex;
# #             align-items: center;
# #             gap: 12px;
# #             padding: 0.5rem 0;
# #         }}

# #         .dash-logo {{
# #             height: 70px;
# #             border-radius: 18px;
# #             box-shadow: 0 8px 24px rgba(88,101,242,0.25);
# #             animation: dashLogoIn 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) both;
# #         }}

# #         .dash-title-wrap {{
# #             animation: dashTitleIn 0.5s ease 0.15s both;
# #         }}

# #         .dash-title {{
# #             font-family: 'Syne', sans-serif;
# #             font-weight: 900;
# #             font-size: 1.85rem;
# #             line-height: 0.9;
# #             background: linear-gradient(135deg, #5865F2, #EB459E);
# #             -webkit-background-clip: text;
# #             -webkit-text-fill-color: transparent;
# #             background-clip: text;
# #             letter-spacing: -0.02em;
# #             margin: 0;
# #         }}

# #         .dash-sub {{
# #             font-family: 'DM Sans', sans-serif;
# #             font-size: 0.72rem;
# #             color: #9ca3c4;
# #             letter-spacing: 0.1em;
# #             text-transform: uppercase;
# #             margin-top: 2px;
# #         }}
# #         </style>

# #         <div class='dash-header'>
# #             <img src='{logo_url}' class='dash-logo' />
# #             <div class='dash-title-wrap'>
# #                 <div class='dash-title'>AI<br/>RollCall</div>
# #                 <div class='dash-sub'>by Khushi</div>
# #             </div>
# #         </div>
# #     """, unsafe_allow_html=True)
# import streamlit as st

# # ─────────────────────────────────────────────────────────────
# #  LOGO — paste your dot PNG URL here (e.g. from imgbb / drive)
# LOGO_URL = "YOUR_DOT_PNG_URL_HERE"
# # ─────────────────────────────────────────────────────────────


# def header_home():
#     st.markdown(f"""
#         <style>
#         @keyframes logoEntrance {{
#             0%   {{ opacity: 0; transform: scale(0.5) rotate(-10deg); }}
#             60%  {{ transform: scale(1.1) rotate(2deg); }}
#             100% {{ opacity: 1; transform: scale(1) rotate(0deg); }}
#         }}
#         @keyframes titleReveal {{
#             from {{ opacity: 0; letter-spacing: 0.5em; }}
#             to   {{ opacity: 1; letter-spacing: -0.03em; }}
#         }}
#         @keyframes taglineSlide {{
#             from {{ opacity: 0; transform: translateY(10px); }}
#             to   {{ opacity: 1; transform: translateY(0); }}
#         }}
#         @keyframes glowPulse {{
#             0%, 100% {{ filter: drop-shadow(0 0 15px rgba(88,101,242,0.4)); }}
#             50%       {{ filter: drop-shadow(0 0 30px rgba(235,69,158,0.5)); }}
#         }}
#         @keyframes badgePop {{
#             from {{ opacity: 0; transform: scale(0); }}
#             to   {{ opacity: 1; transform: scale(1); }}
#         }}

#         .hero-wrapper {{
#             display: flex;
#             flex-direction: column;
#             align-items: center;
#             justify-content: center;
#             padding: 3rem 1rem 2rem;
#             text-align: center;
#             position: relative;
#         }}

#         .logo-ring {{
#             position: relative;
#             display: inline-block;
#             animation: logoEntrance 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) both;
#         }}

#         .logo-ring::before {{
#             content: '';
#             position: absolute;
#             inset: -12px;
#             border-radius: 50%;
#             background: conic-gradient(from 0deg, #5865F2, #EB459E, #5865F2);
#             animation: glowPulse 3s ease-in-out infinite;
#             z-index: 0;
#             padding: 3px;
#             -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - 3px), black 0);
#         }}

#         .logo-img {{
#             height: 100px;
#             width: 100px;
#             object-fit: contain;
#             position: relative;
#             z-index: 1;
#             border-radius: 50%;
#         }}

#         .hero-title {{
#             font-family: 'Syne', sans-serif !important;
#             font-weight: 900 !important;
#             font-size: 4rem !important;
#             line-height: 0.95 !important;
#             background: linear-gradient(135deg, #ffffff 0%, #c4c8ff 50%, #ff9dd5 100%);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             background-clip: text;
#             margin: 1rem 0 0.25rem !important;
#             animation: titleReveal 0.7s cubic-bezier(0.16, 1, 0.3, 1) 0.3s both;
#             letter-spacing: -0.03em;
#         }}

#         .hero-tagline {{
#             font-family: 'DM Sans', sans-serif;
#             font-size: 0.95rem;
#             color: rgba(255,255,255,0.6);
#             letter-spacing: 0.08em;
#             text-transform: uppercase;
#             animation: taglineSlide 0.6s ease 0.6s both;
#             margin-bottom: 0.5rem;
#         }}

#         .creator-badge {{
#             display: inline-flex;
#             align-items: center;
#             gap: 6px;
#             background: rgba(255,255,255,0.08);
#             border: 1px solid rgba(255,255,255,0.15);
#             backdrop-filter: blur(10px);
#             padding: 6px 16px;
#             border-radius: 50px;
#             font-family: 'DM Sans', sans-serif;
#             font-size: 0.8rem;
#             color: rgba(255,255,255,0.7);
#             -webkit-text-fill-color: rgba(255,255,255,0.7);
#             margin-top: 0.75rem;
#             animation: badgePop 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) 0.9s both;
#         }}

#         .creator-badge span {{
#             background: linear-gradient(135deg, #c4c8ff, #ff9dd5);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             background-clip: text;
#             font-weight: 600;
#         }}
#         </style>

#         <div class="hero-wrapper">
#             <div class="logo-ring">
#                 <img src='{LOGO_URL}' class='logo-img' />
#             </div>
#             <h1 class='hero-title'>AI<br/>RollCall</h1>
#             <p class='hero-tagline'>AI-Powered Attendance</p>
#             <div class='creator-badge'>✦ crafted by <span>Khushi</span></div>
#         </div>
#     """, unsafe_allow_html=True)


# def header_dashboard():
#     st.markdown(f"""
#         <style>
#         @keyframes dashLogoIn {{
#             from {{ opacity: 0; transform: scale(0.7) rotate(-5deg); }}
#             to   {{ opacity: 1; transform: scale(1) rotate(0deg); }}
#         }}
#         @keyframes dashTitleIn {{
#             from {{ opacity: 0; transform: translateX(-15px); }}
#             to   {{ opacity: 1; transform: translateX(0); }}
#         }}

#         .dash-header {{
#             display: flex;
#             align-items: center;
#             gap: 12px;
#             padding: 0.5rem 0;
#         }}

#         .dash-logo {{
#             height: 70px;
#             width: 70px;
#             object-fit: contain;
#             border-radius: 18px;
#             box-shadow: 0 8px 24px rgba(88,101,242,0.25);
#             animation: dashLogoIn 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) both;
#         }}

#         .dash-title-wrap {{
#             animation: dashTitleIn 0.5s ease 0.15s both;
#         }}

#         .dash-title {{
#             font-family: 'Syne', sans-serif;
#             font-weight: 900;
#             font-size: 1.85rem;
#             line-height: 0.9;
#             background: linear-gradient(135deg, #5865F2, #EB459E);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             background-clip: text;
#             letter-spacing: -0.02em;
#             margin: 0;
#         }}

#         .dash-sub {{
#             font-family: 'DM Sans', sans-serif;
#             font-size: 0.72rem;
#             color: #9ca3c4;
#             -webkit-text-fill-color: #9ca3c4;
#             letter-spacing: 0.1em;
#             text-transform: uppercase;
#             margin-top: 2px;
#         }}
#         </style>

#         <div class='dash-header'>
#             <img src='{LOGO_URL}' class='dash-logo' />
#             <div class='dash-title-wrap'>
#                 <div class='dash-title'>AI<br/>RollCall</div>
#                 <div class='dash-sub'>by Khushi</div>
#             </div>
#         </div>
#     """, unsafe_allow_html=True)
import streamlit as st
import base64
from pathlib import Path


def _logo_base64():
    logo_path = Path("logo.png")
    if logo_path.exists():
        data = logo_path.read_bytes()
        b64 = base64.b64encode(data).decode()
        return f"data:image/png;base64,{b64}"
    return ""


def header_home():
    logo_src = _logo_base64()
    logo_html = f'<img src="{logo_src}" class="logo-img" />' if logo_src else \
        '<div style="width:62px;height:62px;background:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:13px;color:#1B2A4A;font-family:Arial">AI</div>'

    st.markdown(f"""
        <style>
        @keyframes logoPopIn {{
            0%   {{ opacity:0; transform:scale(0.4) rotate(-12deg); }}
            70%  {{ transform:scale(1.07) rotate(2deg); }}
            100% {{ opacity:1; transform:scale(1) rotate(0deg); }}
        }}
        @keyframes spinRing {{ from{{transform:rotate(0deg)}} to{{transform:rotate(360deg)}} }}
        @keyframes heroIn {{ from{{opacity:0;transform:translateY(16px)}} to{{opacity:1;transform:translateY(0)}} }}
        @keyframes badgePop {{ from{{opacity:0;transform:scale(0.7)}} to{{opacity:1;transform:scale(1)}} }}

        .hero-wrapper {{
            display:flex; flex-direction:column; align-items:center;
            padding:2.5rem 1rem 0.8rem; text-align:center;
        }}
        .logo-ring-wrap {{
            position:relative; width:120px; height:120px; margin:0 auto 1.2rem;
            animation:logoPopIn 0.85s cubic-bezier(0.34,1.56,0.64,1) both;
        }}
        .logo-ring-svg {{
            position:absolute; inset:0; width:120px; height:120px;
            animation:spinRing 7s linear infinite;
        }}
        .logo-img-wrap {{
            position:absolute; inset:13px; border-radius:50%;
            background:#ffffff;
            display:flex; align-items:center; justify-content:center;
            box-shadow:0 6px 28px rgba(0,0,0,0.45);
            overflow:hidden;
        }}
        .logo-img {{
            width:100%; height:100%; object-fit:contain; padding:5px;
        }}
        .hero-title-new {{
            font-family:'Syne',sans-serif; font-weight:900;
            font-size:3.6rem; line-height:0.93; text-align:center;
            background:linear-gradient(135deg, #ffffff 0%, #ffb3d1 35%, #c4a0ff 60%, #80efcc 100%);
            -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
            margin:0 0 0.4rem;
            animation:heroIn 0.7s ease 0.3s both;
            letter-spacing:-0.03em;
        }}
        .hero-tagline-new {{
            font-family:'DM Sans',sans-serif; font-size:0.82rem;
            color:rgba(255,255,255,0.4); -webkit-text-fill-color:rgba(255,255,255,0.4);
            letter-spacing:0.14em; text-transform:uppercase;
            animation:heroIn 0.6s ease 0.45s both;
        }}
        .creator-badge {{
            display:inline-flex; align-items:center; gap:6px;
            background:rgba(255,255,255,0.05);
            border:1px solid rgba(255,255,255,0.1);
            padding:5px 16px; border-radius:50px;
            font-family:'DM Sans',sans-serif; font-size:0.76rem;
            color:rgba(255,255,255,0.5); -webkit-text-fill-color:rgba(255,255,255,0.5);
            margin-top:0.6rem;
            animation:badgePop 0.5s cubic-bezier(0.34,1.56,0.64,1) 0.7s both;
        }}
        .creator-badge span {{
            background:linear-gradient(135deg, #ffd580, #ff9dd5);
            -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
            font-weight:700;
        }}
        </style>

        <div class="hero-wrapper">
            <div class="logo-ring-wrap">
                <svg class="logo-ring-svg" viewBox="0 0 120 120" fill="none">
                    <defs>
                        <linearGradient id="rg2" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%"   stop-color="#ff3c78"/>
                            <stop offset="33%"  stop-color="#a855f7"/>
                            <stop offset="66%"  stop-color="#1ab8ff"/>
                            <stop offset="100%" stop-color="#00e0a0" stop-opacity="0.25"/>
                        </linearGradient>
                    </defs>
                    <circle cx="60" cy="60" r="54" stroke="url(#rg2)"
                        stroke-width="3.5" stroke-linecap="round"
                        stroke-dasharray="220 128" fill="none"/>
                </svg>
                <div class="logo-img-wrap">
                    {logo_html}
                </div>
            </div>
            <div class="hero-title-new">AI<br/>RollCall</div>
            <div class="hero-tagline-new">✦ AI-Powered Attendance ✦</div>
            <div class="creator-badge">crafted by <span>Khushi</span></div>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    logo_src = _logo_base64()
    logo_html = f'<img src="{logo_src}" class="dash-logo" />' if logo_src else \
        '<div style="width:64px;height:64px;background:#1B2A4A;border-radius:16px;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:1rem;color:#C9A84C;font-family:Arial">AI</div>'

    st.markdown(f"""
        <style>
        @keyframes dashLogoIn {{
            from{{opacity:0;transform:scale(0.75) rotate(-4deg)}}
            to{{opacity:1;transform:scale(1) rotate(0deg)}}
        }}
        @keyframes dashTitleIn {{
            from{{opacity:0;transform:translateX(-12px)}}
            to{{opacity:1;transform:translateX(0)}}
        }}
        .dash-header {{
            display:flex; align-items:center; gap:14px; padding:0.4rem 0;
        }}
        .dash-logo {{
            height:68px; width:68px; object-fit:contain;
            border-radius:16px; background:#ffffff; padding:4px;
            box-shadow:0 6px 20px rgba(0,0,0,0.12);
            animation:dashLogoIn 0.5s cubic-bezier(0.34,1.56,0.64,1) both;
        }}
        .dash-title-wrap {{ animation:dashTitleIn 0.5s ease 0.15s both; }}
        .dash-app-name {{
            font-family:'Syne',sans-serif; font-weight:900;
            font-size:1.7rem; line-height:0.92;
            background:linear-gradient(135deg, #ff3c78, #a855f7, #1ab8ff);
            -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
            letter-spacing:-0.02em; margin:0;
        }}
        .dash-sub {{
            font-family:'DM Sans',sans-serif; font-size:0.7rem;
            color:#9ca3c4; -webkit-text-fill-color:#9ca3c4;
            letter-spacing:0.1em; text-transform:uppercase; margin-top:3px;
        }}
        </style>
        <div class='dash-header'>
            {logo_html}
            <div class='dash-title-wrap'>
                <div class='dash-app-name'>AI<br/>RollCall</div>
                <div class='dash-sub'>by Khushi</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
