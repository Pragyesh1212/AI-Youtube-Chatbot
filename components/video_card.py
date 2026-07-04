import streamlit as st


def format_duration(seconds):

    if seconds is None:
        return "Unknown"

    minutes = seconds // 60
    seconds = seconds % 60

    return f"{minutes} min {seconds} sec"


def render_video_card():

    metadata = st.session_state.metadata

    if metadata is None:
        return

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image(
            metadata["thumbnail"],
            use_container_width=True
        )

    with col2:

        st.markdown(f"## {metadata['title']}")

        st.write(
            f"👤 **Channel:** {metadata['channel']}"
        )

        st.write(
            f"⏱ **Duration:** {format_duration(metadata['duration'])}"
        )

    st.divider()