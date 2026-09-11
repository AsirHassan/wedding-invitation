import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Arham & Abeera",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    .stApp {
        margin: 0;
        padding: 0;
    }

    .block-container {
        padding: 0 !important;
        max-width: none !important;
    }

    iframe {
        display: block;
        width: 100% !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

html = Path("index.html").read_text(encoding="utf-8")

st.components.v1.html(
    html,
    height=900,
    scrolling=False,
)