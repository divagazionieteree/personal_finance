import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
from io import StringIO

st.set_page_config(
    page_title="Grafici",
    page_icon="👋",
    layout="wide"
)

data = st.session_state.data
personal_data = st.session_state.personal_data

data.sort_values(by=['Data'], inplace = True)


data["Somme"][0] = personal_data["saldo_iniziale"] - data["Soldi"][0]

for indice in range(len(data)):
    if indice == 0:
      data["Somme"][0] = personal_data["saldo_iniziale"] - data["Soldi"][0]
    else:
       data["Somme"][indice] = data["Somme"][indice - 1] + data["Soldi"][indice]  


fig1, ax1 = plt.subplots(figsize=(40,10))
ax1.set_xlabel('Data')
ax1.set_ylabel('Somme')
ax1.set_title('Fatturato')

rect1_2 = ax1.plot(data["Data"], data["Somme"], label = "2024 Tmin")
ax1.legend()

st.pyplot(fig1)

#st.write(personal_data)

#st.table(data)