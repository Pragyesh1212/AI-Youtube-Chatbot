import time
import streamlit as st


def stream_response(text: str):
    """
    Stream the response word by word.
    """

    placeholder = st.empty()

    words = text.split()

    current = ""

    for word in words:

        current += word + " "

        placeholder.markdown(current + "▌")

        time.sleep(0.02)

    placeholder.markdown(current)

    return current


def render_chat():

    # Show previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    prompt = st.chat_input(
        "Ask anything about this YouTube video..."
    )

    if not prompt:
        return

    # ---------------------------
    # USER MESSAGE
    # ---------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # ---------------------------
    # AI RESPONSE
    # ---------------------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            st.write("Current Session:", st.session_state.video_id)

            answer = st.session_state.chain.invoke(
                prompt,
                config={
                    "configurable": {
                        "session_id": st.session_state.video_id
                    }
                },
            )

        streamed = stream_response(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": streamed,
        }
    )