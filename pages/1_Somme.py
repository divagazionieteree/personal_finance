import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

st.set_page_config(
    page_title="Somme",
    page_icon="👋",
    layout="wide"
)

data = st.session_state.data

gb2=data.groupby(['Tipologia'])
st.table(gb2.Soldi.sum())

gb2=data.groupby(['Tipologia','Società'])
st.table(gb2.Soldi.sum())

