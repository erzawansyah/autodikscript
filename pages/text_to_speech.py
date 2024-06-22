import streamlit as st
from controllers.text_to_speech import input, action, output
from helpers.page_config import page_settings, Session

# from controllers.text_to_speech import input, action, output

tts = page_settings(
    key="tts",
    title="Convert Text to Speech",
    icon="🔊",
    description="This page will help you convert text to speech. Enter the text you want to convert, then click the convert button to generate the audio file.",
    default_state={
        "text": "",
        "selected_vocal": "shimmer",  # "shimmer", "nova", "alloy", "echo", "fable", "onyx"
        "mode": "partial",  # "partial", "full"
        "quality": "standard",  # "standard", "hd quality"
        "audio_files": [],  # ["partial1.mp3", "partial2.mp3", "partial3.mp3", "full.mp3"]
        "full_audio": None,
    },
)

user = Session("user")
output_dir = f"output/{user.get('email')}"

if len(tts.get("audio_files")) > 0:
    output.play(tts.get("full_audio"))
    st.button(
        "Convert Another Text",
        use_container_width=True,
        type="secondary",
        on_click=lambda: (
            tts.reset_key("audio_files"),
            tts.reset_key("full_audio"),
            st.cache_data.clear(),
        ),
    )
    with open(tts.get("full_audio"), "rb") as file:
        st.download_button(
            label="Download Full Audio",
            data=file,
            file_name="full_script.mp3",
            mime="audio/mp3",
            use_container_width=True,
            type="primary",
        )

    if tts.get("mode") == "partial":
        st.download_button(
            label="Download Partial Audio",
            data=output_dir,
            file_name="partial_audio.zip",
            mime="application/zip",
            use_container_width=True,
            type="primary",
        )

else:
    text, vocal, mode, quality = input.form(tts)
    create_audio = st.button("Create Audio", use_container_width=True, type="primary")
    if create_audio:
        try:
            response = action.generate(
                tts,
                text,
                voice=vocal,
                mode=mode,
                hd=quality == "hd quality",
                directory=output_dir,
                filename="speech",
            )
            tts.set("audio_files", response)

            if mode == "full":
                tts.set("full_audio", response[0])
            else:
                merged = output.merge_audio(response, output_dir, "full_audio")
                compress = output.compress(response, output_dir, "partial_audio")
                tts.set("full_audio", merged)

            st.rerun()
        except Exception as e:
            st.error(f"An error occurred: {e}")
