import pandas as pd
import streamlit as st

@st.cache_data
def load_sentences():
    return pd.read_csv("linguaguess/data/audio/sentences.csv")
