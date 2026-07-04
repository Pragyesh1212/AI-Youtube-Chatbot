import streamlit as st

from styles import load_css

from components.header import render_header
from components.sidebar import render_sidebar
from components.video_card import render_video_card
from components.chat import render_chat

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="YouTube AI Chatbot",
    page_icon="🎥",
    layout="wide",
)

st.markdown(load_css(), unsafe_allow_html=True)

# ----------------------------------------------------
# SESSION STATE
# ----------------------------------------------------

defaults = {
    "video_loaded": False,
    "video_url": "",
    "video_id": "",
    "metadata": None,
    "chain": None,
    "messages": [],
}

for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------

render_sidebar()

# ----------------------------------------------------
# MAIN
# ----------------------------------------------------

render_header()

if not st.session_state.video_loaded:

    st.info(
        "👈 Paste a YouTube URL in the sidebar and click **Load Video**."
    )

    st.stop()

render_video_card()

render_chat()