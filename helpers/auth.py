import jwt
import time
import streamlit as st
from supabase import create_client, Client
from streamlit_cookies_controller import CookieController


class AuthManager:
    def __init__(self):
        self.cookie_name = st.secrets["cookies"]["name"]
        self.cookies = CookieController()
        self.supabase_url = st.secrets["supabase_url"]
        self.supabase_anonkey = st.secrets["supabase_anonkey"]
        self.jwt_secret = st.secrets["supabase_jwt_secret"]
        self.jwt_algorithm = st.secrets["supabase_jwt_algorithm"]

    def get_auth_cookie(self):
        return self.cookies.get(f"{self.cookie_name}_token")

    def set_auth_cookie(self, token):
        self.cookies.set(f"{self.cookie_name}_token", token)

    def remove_auth_cookie(self):
        self.cookies.remove(f"{self.cookie_name}_token")

    def create_supabase_client(self, token=None) -> Client:
        return create_client(self.supabase_url, token or self.supabase_anonkey)

    def supabase_login(self, email, password):
        supabase = self.create_supabase_client()
        try:
            response = supabase.auth.sign_in_with_password(
                {"email": email, "password": password}
            )
            return True, response.model_dump()["session"]["access_token"]
        except Exception as e:
            return False, str(e)

    def supabase_logout(self, token):
        supabase = self.create_supabase_client(token)
        try:
            response = supabase.auth.sign_out()
            return True, response.model_dump()
        except Exception as e:
            return False, str(e)

    def supabase_verify(self, auth_token):
        try:
            decoded_token = jwt.decode(
                auth_token,
                self.jwt_secret,
                do_verify=True,
                algorithms=[self.jwt_algorithm],
                audience="authenticated",
                leeway=1,
            )
            is_valid = (
                decoded_token
                if decoded_token["exp"] >= time.time()
                and decoded_token["iat"] <= time.time()
                else None
            )
            return bool(is_valid), decoded_token
        except Exception:
            return False, None

    def login(self, email, password):
        is_login, token = self.supabase_login(email, password)
        if is_login:
            self.set_auth_cookie(token)
        return is_login, token

    def logout(self):
        token = self.get_auth_cookie()
        self.remove_auth_cookie()
        self.supabase_logout(token)

    def verify_token(self):
        token = self.get_auth_cookie()
        is_valid, data = self.supabase_verify(token)
        user = (
            {"email": data["email"], "token": token}
            if is_valid
            else {"email": None, "token": None}
        )
        return is_valid, user
