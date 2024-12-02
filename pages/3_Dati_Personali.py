import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
from io import StringIO
import datetime
import json

st.set_page_config(
    page_title="Dati Personali",
    page_icon="👋",
    layout="wide"
)

if "personal_data" not in st.session_state:
    personal_data = {
      "name": "",
      "date_birth": datetime.date(2010, 1, 1),
      "saldo_iniziale":0,
    }
else:
    personal_data = st.session_state.personal_data

uploaded_json = st.file_uploader("Choose a JSON file")

print(uploaded_json)

if uploaded_json:
    stringio = StringIO(uploaded_json.getvalue().decode("utf-8"))
    stringio.seek(0)
    string_json = stringio.read()
    personal_data_str = json.loads(string_json)
    personal_data = eval(personal_data_str)
        
    if personal_data not in st.session_state:
        st.session_state.personal_data = personal_data

st.divider()
name = st.text_input("insert Name", value = personal_data["name"])
date_birth = st.date_input("When's your birthday", value =  personal_data["date_birth"], min_value = datetime.date(1920, 1, 1), max_value = datetime.date(2023, 12, 31))

st.divider()

saldo_iniziale = st.number_input("Saldo", value = personal_data["saldo_iniziale"])

personal_data = {
  "name": name,
  "date_birth": date_birth,
  "saldo_iniziale":saldo_iniziale,
}

st.session_state.personal_data = personal_data  
st.divider()

st.download_button(label="Download json", data=json.dumps(str(personal_data)), file_name="personal_data.json")