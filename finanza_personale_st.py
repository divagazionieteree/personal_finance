import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import json
from io import StringIO

st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide"
)

st.title('Finanza Personale')

uploaded_files = st.file_uploader("Choose a CSV file")

print(uploaded_files)

data = pd.DataFrame()

if uploaded_files:
    data = pd.read_csv(uploaded_files, sep=',')
    data["Soldi"] = pd.to_numeric(data["Soldi"].str.replace(",", "."))
    data['Data'] = pd.to_datetime(data['Data'],format='%d/%m/%Y') #converto le date    
    data.insert(1, "Month", 0)
    data.insert(2, "Year", 0)
    data.insert(6, "Somme", 0)
    data["Year"] = data["Data"].apply(lambda x: x.year)
    data["Month"] = data["Data"].apply(lambda x: x.month)

    data.sort_values(by=['Data'],ascending = False, inplace = True)

    st.table(data)
        
    if data not in st.session_state:
        st.session_state.data = data
        st.write(st.session_state.data)

if "data" not in st.session_state:
    st.write("Tabella non presente")
else:
    data = st.session_state.data
    st.table(data)