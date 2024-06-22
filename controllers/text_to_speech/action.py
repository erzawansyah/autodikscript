import os
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai_api_key"])


def output_directory_handler(output_dir, is_partial=False):
    output_dir_partials = f"{output_dir}/partials"

    if is_partial:
        if not os.path.exists(output_dir_partials):
            os.makedirs(output_dir_partials)
        return output_dir_partials

    return output_dir


@st.cache_data
def openai_request(
    text: str,
    voice: str = "shimmer",
    hd: str = False,
    directory: str = "output",
    filename: str = "script",
):
    speech_file_path = directory + "/" + filename + ".mp3"
    response = client.audio.speech.create(
        model="tts-1-hd" if hd else "tts-1",
        voice=voice,
        input=text,
    )
    try:
        response.write_to_file(speech_file_path)
        return speech_file_path
    except Exception as e:
        return str(e)


def partial_text_handler(text):
    """
    This will split the text based on the new line character.

    Returns:
        list: A list of partial texts.
    """
    # remove double line breaks
    text = text.replace("\n\n", "\n")
    text = text.replace("\r\n", "\n")
    split_text = text.split("\n")

    # remove empty strings
    return [t.strip() for t in split_text if t.strip()]


def generate(
    tts,
    text: str,
    voice: str = "shimmer",
    mode: str = "full",
    hd: str = False,
    directory: str = "output",
    filename: str = "script",
):
    tts.set("text", text)
    tts.set("selected_vocal", voice)
    tts.set("mode", mode)
    tts.set("quality", "hd quality" if hd else "standard")

    directory = output_directory_handler(directory, mode == "partial")
    result_container = []
    if mode == "full":
        result_container.append(openai_request(text, voice, hd, directory, filename))
    else:
        partial_texts = partial_text_handler(text)
        for i, partial_text in enumerate(partial_texts):
            result_container.append(
                openai_request(
                    partial_text,
                    voice,
                    hd,
                    directory,
                    f"partial_{i}",
                )
            )
    return result_container
