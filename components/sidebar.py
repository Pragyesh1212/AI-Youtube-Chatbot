import streamlit as st

from utils import extract_video_id
from transcript import get_transcript
from vector_store import create_vector_store
from rag import build_rag_chain
from services.metadata import get_video_metadata


def render_sidebar():
    """
    Render sidebar and load YouTube video.
    """

    with st.sidebar:

        st.title("🎥 YouTube AI")

        st.markdown("---")

        url = st.text_input(
            "Paste YouTube URL",
            value=st.session_state.get("video_url", ""),
            placeholder="https://www.youtube.com/watch?v=..."
        )

        load = st.button(
            "🚀 Load Video",
            use_container_width=True
        )

        if load:

            if not url.strip():

                st.warning("Please enter a YouTube URL.")

                return

            try:

                with st.spinner("Loading video..."):

                    video_id = extract_video_id(url)

                    transcript = get_transcript(video_id)

                    vector_store = create_vector_store(
                        transcript,
                        video_id
                    )

                    chain = build_rag_chain(
                        vector_store
                    )

                    metadata = get_video_metadata(
                        url
                    )

                    st.session_state.video_url = url
                    st.session_state.video_id = video_id
                    st.session_state.metadata = metadata
                    st.session_state.chain = chain
                    st.session_state.video_loaded = True
                    st.session_state.messages = []

                st.success("Video Loaded Successfully!")

            except Exception as e:

                st.error(str(e))

        st.markdown("---")

        if st.button(
            "🗑 Clear Chat",
            use_container_width=True
        ):

            st.session_state.messages = []

        if st.button(
            "🔄 Load Another Video",
            use_container_width=True
        ):

            st.session_state.video_loaded = False
            st.session_state.video_url = ""
            st.session_state.video_id = ""
            st.session_state.metadata = None
            st.session_state.chain = None
            st.session_state.messages = []

            st.rerun()

        st.markdown("---")

        st.caption("⚡ Powered by Groq + HuggingFace + FAISS")