import streamlit as st


def logout_button(session, auth_manager):
    if st.button("Logout", use_container_width=True, type="primary"):
        session.reset_all()
        auth_manager.logout()
        st.rerun()
