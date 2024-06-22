import os
import streamlit as st
from helpers.auth import AuthManager
from helpers.sessions import init_session
from components.login_form import login_form


def create_user_dir(email):
    """
    Function to create a user directory.
    """
    if not os.path.exists(f"output/{email}"):
        os.makedirs(f"output/{email}")


def remove_user_dir(email):
    """
    Function to remove a user directory.
    """
    if os.path.exists(f"output/{email}"):
        os.rmdir(f"output/{email}")


def main():
    auth_manager = AuthManager()
    session = init_session(auth_manager)
    if session.get("is_login"):
        create_user_dir(session.get("email"))
        st.switch_page("pages/dashboard.py")
    else:
        remove_user_dir(session.get("email"))
        login_form(session, auth_manager)


if __name__ == "__main__":
    main()
