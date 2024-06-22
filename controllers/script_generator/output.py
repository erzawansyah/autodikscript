import os
import streamlit as st


def display(title, raw):
    with st.container():
        st.write(f"### {title}")
        st.write(f"*{raw.hook}*")
        st.divider()
        for scene in raw.body:
            st.write(scene.voiceover)
        st.write(raw.closing.voiceover)
        st.divider()
        st.write(raw.cta.call_to_action)


def save(title, raw, dir="output", filename="script.md"):
    md_content = f"# {title}\n\n"
    md_content += f"*{raw.hook}*\n\n"
    md_content += "---\n\n"
    for scene in raw.body:
        md_content += f"**Scene {raw.body.index(scene) + 1}**\n{scene.voiceover}\n\n"
    md_content += "---\n\n"
    md_content += f"**Closing:**\n{raw.closing.voiceover}\n\n"
    md_content += "---\n\n"
    md_content += f"{raw.cta.call_to_action}\n"
    os.makedirs(dir, exist_ok=True)
    with open(f"{dir}/{filename}", "w") as file:
        file.write(md_content)
