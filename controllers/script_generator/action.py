import streamlit as st
from modules.ai.script_writer import write_script


def generate_script(state, model, title, keywords, notes, total_sections):
    """
    Function to generate a script using the AI model.
    """

    state.set("model", model)
    state.set("title", title)
    state.set("keywords", keywords)
    state.set("notes", notes)
    state.set("total_sections", total_sections)

    try:
        script = write_script(
            keywords=keywords,
            title=title,
            notes=notes,
            model=model,
            total_sections=total_sections,
        )
        return script
    except Exception as e:
        st.toast(f"Error: {e}", type="error")
