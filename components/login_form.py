import time
import streamlit as st


def login_form(session, auth_manager):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        is_login, token = auth_manager.login(email, password)
        if is_login:
            session.set("is_login", True)
            session.set("email", email)
            session.set("token", token)
            st.success("Login Success")
            time.sleep(2)
            st.rerun()
        else:
            st.warning(f"Login Failed. Reason: {token}")
