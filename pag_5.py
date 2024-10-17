import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

st.title("Gráfico de Área")
@st.cache_data
def filter_df(columns):
    if columns:
        return st.session_state.df[columns]
    return st.session_state.df

data_columns = st.session_state.df.columns.tolist()
selected_columns = st.sidebar.multiselect(
    'Selecione as colunas para o gráfico:',
    options=data_columns,
    default=data_columns
)

filtered_df = filter_df(selected_columns)
st.area_chart(filtered_df)