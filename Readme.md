# Autodikscript

> **Status: Archived (2026)**
>
> - **Reason:** a personal prototype that is no longer maintained; it depends on older OpenAI models and libraries and on a Supabase login.
> - **Created:** 2024
> - **What's next:** the idea continues as a set of AI web tools that will be built in a new repository.
>
> The code is kept for reference only. Issues and pull requests are not monitored.

Autodikscript ("YT Assets Generator") is a small Streamlit app for YouTube creators with three tools: a **script writer** that turns a title, keywords, and notes into a structured video script (hook, scenes with visual brief and voiceover, closing, call to action); **text to speech** using OpenAI TTS, either as one file or line by line; and an **image prompter** (beta) that turns a script paragraph into image-generation prompts.

Stack: Python, Streamlit 1.36, LangChain + OpenAI (`gpt-3.5-turbo` / `gpt-4o`, `tts-1`), moviepy, Supabase auth. To try it locally you need Python 3.12, `pip install -r requirements.txt`, a `.streamlit/secrets.toml` with your own OpenAI and Supabase settings, and `streamlit run app.py`. It is not expected to work with current library versions without changes.
