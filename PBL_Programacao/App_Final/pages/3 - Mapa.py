import numpy as np
import pandas as pd
import streamlit as st

st.header('Painel de Monitoramento Microbiológico')

# Upload do arquivo CSV
upload_arquivo = st.file_uploader('Escolha um arquivo (.csv):', type='csv')

# Subheader
st.header('Mapa', divider='rainbow')

if upload_arquivo is not None:

    # Leitura do arquivo CSV
    arquivo = pd.read_csv(upload_arquivo)

    # Filtrando dados (apenas um teste aqui)
    arquivo_filt = arquivo.dropna().query('ds_micro_organismo')

    arquivo = arquivo_filt.astype({'Latitude':-23.6005556, 'Longitude':-46.7152778})

    # Mostrando mapa para o usuário
    st.map(data = arquivo_filt, latitude = 'Latitude', longitude = 'Longitude')