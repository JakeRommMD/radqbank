# radqbank/auth.py
import streamlit as st
from radqbank.auth import login

def get_supabase():
    if "supabase" not in st.session_state:
        url = st.secrets["supabase_url"]
        key = st.secrets["supabase_key"]
        st.session_state.supabase = create_client(url, key)
    return st.session_state.supabase

def login(email, password):
    supabase = get_supabase()
    res = supabase.auth.sign_in_with_password(
        {"email": email, "password": password})
    st.session_state.user = res.user
