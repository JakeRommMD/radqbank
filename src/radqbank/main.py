# radqbank/main.py
import streamlit as st
from .state import get_cfg

cfg = get_cfg()
st.set_page_config(page_title=cfg["app_title"],
                   page_icon="📚",
                   layout="wide")

st.sidebar.title(cfg["app_title"])
st.sidebar.page_link("radqbank/main.py", label="🏠 Dashboard")
st.sidebar.page_link("radqbank/pages/qsession.py", label="❓ Question Session")
st.sidebar.page_link("radqbank/pages/review.py",   label="📊 Review")

st.header("Dashboard (MVP)")
st.write("Welcome!  Your progress will appear here once Phase 2 lands.")
