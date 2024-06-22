import streamlit as st


def form(**kwargs):
    with st.expander("Advanced Options"):
        model = st.selectbox(
            "Select the model",
            [
                "gpt-3.5-turbo",
                "gpt-4o",
            ],
            index=0,
            key="__script_model__",
        )
        total_sections = st.number_input(
            "Enter the number of sections for the script",
            min_value=1,
            max_value=20,
            value=kwargs.get("total_sections", 10),
            key="__script_total_sections__",
        )

    title = st.text_input(
        "Enter the title for youtube script",
        placeholder="eg. Why Am I Seeing This Everywhere? The Baader-Meinhof Phenomenon Explained",
        value=kwargs.get("title", ""),
        key="__script_title__",
    )
    keywords = st.text_input(
        "Enter the keywords for youtube script. Separate the keywords with a comma.",
        placeholder="eg. Baader-Meinhof Phenomenon, Seeing Everywhere",
        value=kwargs.get("keywords", ""),
        key="__script_keywords__",
    )
    notes = st.text_area(
        "Enter any notes for the script",
        placeholder="eg. Please include the history of the Baader-Meinhof Phenomenon in the script.",
        value=kwargs.get("notes", ""),
        help="Add any additional notes for the script. This will help the AI generate a more customized script based on your requirements.",
        key="__script_notes__",
    )
    return model, title, keywords, notes, total_sections
