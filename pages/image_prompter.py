import streamlit as st
from helpers.page_config import page_settings
from controllers.image_prompter import action

img_prompt = page_settings(
    key="img_prompt",
    title="Generate Image Prompt",
    icon="🖼️",
    description="This page will help you generate an image prompt. Enter the text you want to convert, then click the generate button to generate the image prompt.",
    default_state={
        "text": "",
        "prompt_count": 4,
        "result": [],
    },
)


if len(img_prompt.get("result")) > 0:
    st.markdown("## Generated Image Prompts")
    for i, prompt in enumerate(img_prompt.get("result")):
        st.markdown(f"""Prompt {i + 1}:\n`{prompt}`\n""")

    st.button(
        "Create Another Image Prompt",
        use_container_width=True,
        type="secondary",
        on_click=lambda: (img_prompt.reset_key("result"), st.cache_data.clear()),
    )

else:
    # Textarea input
    # Desc: Enter paragraph and click generate to generate related image prompt for you to use.
    paragraph = st.text_area(
        "Enter paragraph here",
        value=img_prompt.get("text"),
        height=160,
    )
    prompt_count = st.slider(
        "Prompt count",
        1,
        10,
        value=img_prompt.get("prompt_count"),
        help="Select the number of prompts to generate.",
    )
    prompt_button = st.button(
        "Generate",
        use_container_width=True,
        type="primary",
    )

    if prompt_button:
        img_prompt.set("text", paragraph)
        img_prompt.set("prompt_count", prompt_count)
        result = action.prompting(paragraph, prompt_count)
        img_prompt.set("result", result.output)
        st.rerun()

# Warning beta
st.warning("This feature is still in beta. Please report any issues.")
