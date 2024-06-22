import streamlit as st
from moviepy.editor import AudioFileClip, concatenate_audioclips
from moviepy.audio.AudioClip import AudioArrayClip
from zipfile import ZipFile
import numpy as np


def play(audio_file):
    st.audio(audio_file, format="audio/mp3")


def merge_audio(
    files,
    output_dir="output",
    output_filename="full_script",
):
    final_output = f"{output_dir}/{output_filename}.mp3"

    try:
        audio_clips = []
        silence_duration = 0.3  # 300 ms silence
        silence_array = np.zeros((int(44100 * silence_duration), 2))
        silence_clip = AudioArrayClip(silence_array, fps=44100)

        for file in files:
            audio_clips.append(AudioFileClip(file))
            audio_clips.append(silence_clip)

        # Remove the last added silence clip
        audio_clips = audio_clips[:-1]

        final_audio = concatenate_audioclips(audio_clips)
        final_audio.write_audiofile(final_output)
        return final_output
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None


def compress(files, output_dir="output", output_filename="audio_files"):
    try:
        with st.spinner("Compressing audio files..."):
            with ZipFile(f"{output_dir}/{output_filename}.zip", "w") as zipf:
                for file in files:
                    print(file)
                    zipf.write(file)
        return f"{output_dir}/{output_filename}.zip"
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None
