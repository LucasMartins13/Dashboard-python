import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

st.title("Gráfico de Barras")
modo = st.selectbox("Escolha a opção:", ["Uploud", "Ticker", "AutoData"])

lista_acoes = st.sidebar.multiselect("Escolha as ações para visualizar", st.session_state.df.columns)

if modo == "Ticker":
    if lista_acoes:
        dados = st.session_state.df[lista_acoes]
        if len(lista_acoes) == 1:
            acao_unica = lista_acoes[0]
            dados = dados.rename(columns={acao_unica: "Close"})

        data_inicial = dados.index.min().to_pydatetime()
        data_final = dados.index.max().to_pydatetime()
        intervalo_data = st.sidebar.slider(
            "Selecione o período",
            min_value=data_inicial,
            max_value=data_final,
            value=(data_inicial, data_final),
            step=pd.Timedelta(days=1)
        )
        
        dados = dados.loc[intervalo_data[0]:intervalo_data[1]]

        st.bar_chart(dados)

else:
    if lista_acoes:
        dados = st.session_state.df[lista_acoes]
        if len(lista_acoes) == 1:
            acao_unica = lista_acoes[0]
            dados = dados.rename(columns={acao_unica: "Close"})

        st.bar_chart(dados)
