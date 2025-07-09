# radqbank/loaders.py
import duckdb, pandas as pd, streamlit as st
from .state import get_cfg

@st.cache_data
def load_questions():
    cfg = get_cfg()
    df = pd.read_csv(cfg["csv_path"])
    con = duckdb.connect(database=":memory:")
    con.register("questions", df)   # now usable with SQL
    return df, con
