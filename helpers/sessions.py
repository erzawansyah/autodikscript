import streamlit as st


class Session:
    def __init__(self, key, default_value=None):
        self.key = key
        self.default_value = default_value

    def start(self):
        if self.default_value is not None and self.key not in st.session_state:
            st.session_state[self.key] = self.default_value

    def get(self, key):
        return st.session_state[self.key].get(key)

    def set(self, key, value):
        st.session_state[self.key][key] = value

    def reset_key(self, key):
        st.session_state[self.key][key] = self.default_value[key]

    def reset_all(self):
        st.session_state[self.key] = self.default_value


def init_session(auth_manager):
    is_valid, user = auth_manager.verify_token()
    session = Session("user", {"is_login": False, "email": None, "token": None})
    session.start()
    if is_valid:
        session.set("is_login", True)
        session.set("email", user["email"])
        session.set("token", user["token"])
    return session
