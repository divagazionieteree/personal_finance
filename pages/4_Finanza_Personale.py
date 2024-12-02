import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
from io import StringIO
import datetime
import json

st.set_page_config(
    page_title="Finanza Personale",
    page_icon="👋",
    layout="wide"
)

data = st.session_state.data
personal_data = st.session_state.personal_data
tasso_FED = 4.75

data.sort_values(by=['Data'], inplace = True)

st.title('Finanza Personale')

st.divider()

st.write("Data di nascita")
st.write(personal_data["date_birth"])

data_birth = str(personal_data["date_birth"])
difference = datetime.datetime.now() - datetime.datetime.strptime(data_birth, "%Y-%m-%d")
years = int(difference.days / 365)

st.write("Anni")
st.write(years)

st.divider()

st.markdown("### Calcolo base Percentuale Obbligazioni nell'Asset Allocation")

percentuale = 100 - years

st.write(f"Percentuale = {percentuale}%")

st.markdown("### Calcolo THE BULL Percentuale Obbligazioni nell'Asset Allocation")

percentuale = 125 - years - 5 * tasso_FED

st.write(f"Percentuale = {percentuale}%")
