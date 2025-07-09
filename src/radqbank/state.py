# radqbank/state.py
import yaml, pathlib, streamlit as st
ROOT = pathlib.Path(__file__).resolve().parents[2] # repo root (.. / .. /)

def get_cfg():
    if "cfg" not in st.session_state:
        with open(ROOT / "config.yaml") as f:
            st.session_state.cfg = yaml.safe_load(f)
    return st.session_state.cfg
