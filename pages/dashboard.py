import streamlit as st
from helpers.page_config import page_settings
from helpers.sessions import Session

page_settings(
    key="dashboard",
    title="Welcome",
    icon="🎉",
)

user = Session("user")
email = user.get("email")


st.markdown(
    f"""Welcome {email}!
We are excited to have you here. Explore the full range of features we offer to enhance your creative process.

## 📋 Features

### 📝 Generate Script
Create compelling scripts for your YouTube videos effortlessly.
- **How it works:** Enter the keywords and the title for your video, then click the "Generate" button to produce a script tailored to your needs.

### 🔊 Convert Text to Speech
Transform written text into spoken words with ease.
- **How it works:** Enter the text you want to convert, then click the "Convert" button to generate the audio file. Ideal for voiceovers and narrations.

### 🖼️ Generate Image Prompt
Visualize your ideas by converting text into image prompts.
- **How it works:** Enter the descriptive text, then click the "Generate" button to create an image prompt that can guide your visual content creation.

---

Feel free to navigate through these features and make the most out of our platform. If you have any questions or need assistance, our support team is here to help.

Happy creating! 🚀"""
)
