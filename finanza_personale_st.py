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

uploaded_json = st.file_uploader("Choose a JSON file")

print(uploaded_json)


if uploaded_files:
    data = pd.read_csv(uploaded_files, sep=',')
    data["Soldi"] = pd.to_numeric(data["Soldi"].str.replace(",", "."))
    data['Data'] = pd.to_datetime(data['Data'],format='%d/%m/%Y') #converto le date    
    data.insert(1, "Month", 0)
    data.insert(2, "Year", 0)
    data["Year"] = data["Data"].apply(lambda x: x.year)
    data["Month"] = data["Data"].apply(lambda x: x.month)

    data.sort_values(by=['Data'],ascending = False, inplace = True)

    st.table(data)
        
    if data not in st.session_state:
        st.session_state.data = data
        st.write(st.session_state.data)

if uploaded_json:
    stringio = StringIO(uploaded_json.getvalue().decode("utf-8"))
    stringio.seek(0)
    string_json = stringio.read()
    string_json1 = json.loads(string_json)
    st.write(string_json1)
    st.download_button(label="Download json", data=json.dumps(string_json1), file_name="flower.json")



