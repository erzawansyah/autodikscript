import streamlit as st
from sidebar import display_sidebar
from helpers.sessions import Session


def page_settings(key, **kwargs):
    title = kwargs.get("title", "")
    icon = kwargs.get("icon", "📝")
    description = kwargs.get("description", "")
    default_state = kwargs.get("default_state", None)

    st.set_page_config(
        page_title=title,
        page_icon=icon,
    )
    display_sidebar()
    st.title(f"{icon} {title}")
    st.write(description.strip())

    state = Session(key, default_state)
    if key not in st.session_state:
        state.start()
    return state
