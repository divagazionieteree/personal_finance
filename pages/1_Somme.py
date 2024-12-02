import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
from io import StringIO

st.set_page_config(
    page_title="Somme",
    page_icon="👋",
    layout="wide"
)

data = st.session_state.data

gb2=data.groupby(['Tipologia'])
gb2_ser = gb2.Soldi.sum()
gb2_df = gb2_ser.to_frame()

gb2_df.sort_values(by=['Soldi'], inplace = True)
st.table(gb2_df)

gb3=data.groupby(['Tipologia','Società'])
gb3_ser = gb3.Soldi.sum()
gb3_df = gb3_ser.to_frame()
gb3_df.sort_values(by=['Soldi'], inplace = True)
st.table(gb3_df)


