import streamlit as st
from helpers.page_config import page_settings, Session
from controllers.script_generator import input, action, output


state = page_settings(
    key="script",
    title="Generate Script",
    icon="📝",
    description="This page will help you generate scripts for your YouTube videos. Enter the keywords and the title for your video, then click the translate button to generate the script.",
    default_state={
        "title": "",
        "keywords": "",
        "notes": "",
        "total_sections": 10,
        "model": "gpt-3.5-turbo",
        "result": None,
    },
)

user = Session("user")
output_dir = f"output/{user.get('email')}"


if state.get("result") is not None:
    with st.container(border=True):
        output.display(state.get("title"), state.get("result"))
    st.button(
        "Regenerate Script",
        use_container_width=True,
        type="secondary",
        on_click=lambda: (state.reset_key("result"), st.cache_data.clear()),
    )
    with open(f"{output_dir}/script.md", "r") as file:
        st.download_button(
            label="Download Script",
            data=file,
            file_name=f"[SCRIPT] - {state.get('title')}.md",
            mime="text/markdown",
            use_container_width=True,
            type="primary",
        )
else:
    model, title, keywords, notes, total_sections = input.form(
        total_sections=state.get("total_sections"),
        model=state.get("model"),
        title=state.get("title"),
        keywords=state.get("keywords"),
        notes=state.get("notes"),
    )

    generate = st.button("Generate Script", use_container_width=True, type="primary")

    if generate:
        try:
            result = action.generate_script(
                state, model, title, keywords, notes, total_sections
            )
            if result:
                state.set("result", result)
                output.save(title, result, dir=f"{output_dir}")
                st.balloons()
                st.rerun()
            else:
                raise Exception("Error generating script.")
        except Exception as e:
            st.error(f"Error: {e}")
            restart = st.button("Try Again", use_container_width=True, type="secondary")
            st.rerun()
