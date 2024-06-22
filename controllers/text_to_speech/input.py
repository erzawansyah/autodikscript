import streamlit as st


def form(tts):
    vocals = ["shimmer", "nova", "alloy", "echo", "fable", "onyx"]
    mode = ["partial", "full"]

    with st.expander("Advanced Settings", expanded=False):
        vocal = st.selectbox(
            "Select the voice",
            vocals,
            format_func=lambda vocal: vocal.title(),
            index=vocals.index(tts.get("selected_vocal")),
            key="__tts_vocal__",
        )
        st.caption(
            "To hear the example of each voice, visit the [OpenAI Official Web](https://platform.openai.com/docs/guides/text-to-speech/voice-options)"
        )
        mode = st.selectbox(
            "Select the mode",
            mode,
            format_func=lambda mode: mode.title(),
            index=mode.index(tts.get("mode")),
            key="__tts_mode__",
        )
        st.caption(
            "**Partials**: Will split the text into smaller parts and generate audio for each part. This is useful if you have a long text that you want, but it takes longer."
            "**Full**: Generate all the text at once. Useful for shorter texts. If you have a long text, it may impact the quality of the audio."
        )
        quality = st.selectbox(
            "Select the quality",
            ["standard", "hd quality"],
            index=0 if tts.get("quality") == "standard" else 1,
            format_func=lambda quality: quality.title(),
            key="__tts_quality__",
        )

    text = st.text_area(
        "Enter the text you want to convert to speech",
        value=tts.get("text"),
        height=200,
        placeholder="e.g., Welcome to our exploration of the Mere-Exposure Effect and why we are drawn to familiar things. Let's delve into the intriguing world of psychology and human behavior.",
        key="__tts_text__",
    )

    return text, vocal, mode, quality
