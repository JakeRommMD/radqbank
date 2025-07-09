# src/radqbank/loaders.py
import duckdb, pandas as pd, streamlit as st
from radqbank.state import get_cfg

@st.cache_data                 # ✅ only the DataFrame is cached
def load_questions_df():
    cfg = get_cfg()
    return pd.read_csv(cfg["csv_path"])

@st.cache_resource             # ✅ connections are resources, not data
def get_duckdb_conn(df):
    con = duckdb.connect(database=":memory:")
    con.register("questions", df)
    return con

