import streamlit as st


def footer_home():
    st.markdown("""
        <style>
        @keyframes footerFadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        .footer-home {
            margin-top: 3rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
            animation: footerFadeIn 0.6s ease 1s both;
        }

        .footer-home .footer-line {
            font-family: 'DM Sans', sans-serif;
            font-size: 0.82rem;
            color: rgba(255,255,255,0.45);
            letter-spacing: 0.05em;
        }

        .footer-home .footer-khushi {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-family: 'Syne', sans-serif;
            font-weight: 700;
            font-size: 0.9rem;
            background: linear-gradient(135deg, #c4c8ff, #ff9dd5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .footer-home .dot-sep {
            width: 4px;
            height: 4px;
            border-radius: 50%;
            background: rgba(255,255,255,0.25);
            display: inline-block;
            margin: 0 6px;
            vertical-align: middle;
        }
        </style>

        <div class="footer-home">
            <div class="footer-line">
                built with ❤️ 
                <span class="dot-sep"></span>
                <span class="footer-khushi">✦ Khushi</span>
                <span class="dot-sep"></span>
                AI RollCall © 2025
            </div>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <style>
        .footer-dash {
            margin-top: 2.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid rgba(88, 101, 242, 0.12);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }

        .footer-dash .fd-text {
            font-family: 'DM Sans', sans-serif;
            font-size: 0.8rem;
            color: #9ca3c4;
        }

        .footer-dash .fd-name {
            font-family: 'Syne', sans-serif;
            font-weight: 700;
            font-size: 0.85rem;
            background: linear-gradient(135deg, #5865F2, #EB459E);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .footer-dash .fd-dot {
            width: 3px;
            height: 3px;
            border-radius: 50%;
            background: #d1d5f0;
            display: inline-block;
        }
        </style>

        <div class="footer-dash">
            <span class="fd-text">crafted with ❤️ by</span>
            <span class="fd-name">Khushi</span>
            <span class="fd-dot"></span>
            <span class="fd-text">AI-RollCall 2026</span>
        </div>
    """, unsafe_allow_html=True)