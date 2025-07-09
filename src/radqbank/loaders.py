# src/radqbank/loaders.py
import pandas as pd
import duckdb
import streamlit as st

from radqbank.state import get_cfg      # ✅ the only intra-package import

@st.cache_data
def load_questions():
    cfg = get_cfg()
    try:
        df = pd.read_csv(cfg["csv_path"])
        if df.empty:
            st.error("CSV loaded but contains no rows.")
        else:
            con = duckdb.connect(database=":memory:")
            con.register("questions", df)
            return df, con
    except FileNotFoundError:
        st.error(f"CSV not found at {cfg['csv_path']}")
        return pd.DataFrame(), None

