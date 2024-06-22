import streamlit as st
from helpers.auth import AuthManager
from helpers.sessions import Session
from components.logout_button import logout_button


def display_sidebar():
    auth_manager = AuthManager()
    session = Session("user")

    if not session.get("is_login"):
        st.switch_page("app.py")

    pages = [
        "dashboard.py",
        "script_writer.py",
        "text_to_speech.py",
        "image_prompter.py",
    ]
    st.sidebar.title("YT Assets Generator")
    for page in pages:
        st.sidebar.page_link(
            f"pages/{page}", label=page.replace(".py", "").replace("_", " ").title()
        )
    with st.sidebar:
        st.divider()
        logout_button(session, auth_manager)
