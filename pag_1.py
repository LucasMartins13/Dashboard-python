import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

st.title('Home')
st.text('Você prefere usar um arquivo ou dados gerados automaticamente?')
st.text('Caso prefira dados gerados automaticamente, não faça o upload de um arquivo.')

uploaded_file = st.file_uploader('Faça o upload aqui:')
if uploaded_file is not None:
    st.session_state.df = pd.read_csv(uploaded_file)
    st.success("Arquivo carregado com sucesso!")

if 'use_stock_data' not in st.session_state:
    st.session_state.use_stock_data = False

st.text('Se nao quiser dar uploud, pode digitar o ticker de uma ação clicando no botão abaixo')
st.text('Caso nao, aperte o botão "Resetar" no final do pagina')

btn1 = st.button('Bolsa De Valores')
if btn1:
    st.session_state.use_stock_data = True

if st.session_state.use_stock_data:
    ticker = st.text_input(f'Digite o ticker da ação (Ex: AAPL) OBS: Algumas ações nao funcionarao por causa do Yahoo Finance (Ex: PETR4)')
    if ticker:
        ticker = ticker.upper().strip()
        try:
            empresa = yf.Ticker(ticker)
            tickerDF = empresa.history(period='1d', start='2010-01-01', end='2023-12-31')
            if not tickerDF.empty:
                st.session_state.df = tickerDF
                st.success(f"Dados da bolsa de valores carregados com sucesso para {ticker}!")
            else:
                st.error(f"Nenhum dado encontrado para o ticker: {ticker}. Verifique se o ticker está correto.")
        except Exception as e:
            st.error(f"Ocorreu um erro ao buscar o ticker: {ticker}. Detalhes: {e}")


st.text('Caso nao tenha feito Uploud e escolhido uma ação, clique no botao abaixo.')
st.text('Ao clicar no botão estará usando dados FICTICIOS na Dashboard')

btn2 = st.button('Resetar')
if btn2:
    st.session_state.df = pd.DataFrame(
        np.random.rand(10, 3),
        columns=['Preço', 'Taxa de Ocupação', 'Taxa de Inadimplência']
    )
    st.session_state.use_stock_data = False

if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(
        np.random.rand(10, 3),
        columns=['Preço', 'Taxa de Ocupação', 'Taxa de Inadimplência']
    )

st.text('OBS: Se quiser mudar de Ticker para Uploud, aperte no botão "Resetar" antes')

if 'df' in st.session_state and not st.session_state.df.empty:
    data_columns = st.session_state.df.columns.tolist()
    st.write('Aqui estão as colunas do DataFrame:', data_columns)