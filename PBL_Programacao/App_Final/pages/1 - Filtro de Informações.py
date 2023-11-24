import pandas as pd
import streamlit as st

# Header
st.header('Painel de Monitoramento Microbiológico')

# Upload do arquivo CSV
upload_arquivo = st.file_uploader('Escolha um arquivo (.csv):', type='csv')

# Subheader
st.subheader('Tabela Interativa de Dados', divider='rainbow')

if upload_arquivo is not None:

    # Leitura do arquivo CSV
    arquivo = pd.read_csv(upload_arquivo)
    
    # Criando um filtro de dados para dia e hora de admissão do paciente
    dh_admissao_paciente = st.selectbox('Selecione o dia e horário de admissão do paciente: ', ['Todos'] + list(arquivo['dh_admissao_paciente'].unique()))

    if dh_admissao_paciente == 'Todos':

        arquivo_filt = arquivo

    else:

        arquivo_filt = arquivo[arquivo['dh_admissao_paciente'] == dh_admissao_paciente]

    # Criando um filtro de dados para dia e hora de alta do paciente
    dh_alta_paciente = st.selectbox('Selecione o dia e horário de alta do paciente: ', ['Todos'] + list(arquivo['dh_alta_paciente'].unique()))

    if dh_alta_paciente != 'Todos':

        arquivo_filt = arquivo_filt[arquivo_filt['dh_alta_paciente'] == dh_alta_paciente]

    # Criando um filtro de dados para área de encontro com o paciente
    tipo_encontro = st.selectbox('Selecione a área de encontro: ', ['Todos'] + list(arquivo['ds_tipo_encontro'].unique()))

    if tipo_encontro != 'Todos':

        arquivo_filt = arquivo_filt[arquivo_filt['ds_tipo_encontro'] == tipo_encontro]

    # Criando um filtro de dados para a abreviação do nome do tipo de exame
    ds_alias_exame_millennium_3 = st.selectbox('Selecione o tipo de exame: ', ['Todos'] + list(arquivo['ds_alias_exame_millennium_3'].unique()))

    if ds_alias_exame_millennium_3 != 'Todos':

        arquivo_filt = arquivo_filt[arquivo_filt['ds_alias_exame_millennium_3'] == ds_alias_exame_millennium_3]

    # Criando um filtro de dados para a unidade de coleta do exame
    ds_unidade_coleta = st.selectbox('Selecione a unidade de coleta do exame: ', ['Todos'] + list(arquivo['ds_unidade_coleta'].unique()))

    if ds_unidade_coleta != 'Todos':

        arquivo_filt = arquivo_filt[arquivo_filt['ds_unidade_coleta'] == ds_unidade_coleta]

    # Criando um filtro de dados para dia e hora da coleta do exame
    dh_coleta_exame = st.selectbox('Selecione o dia e horário da coleta do exame: ', ['Todos'] + list(arquivo['dh_coleta_exame'].unique()))

    if dh_coleta_exame != 'Todos':

        arquivo_filt = arquivo_filt[arquivo_filt['dh_coleta_exame'] == dh_coleta_exame]

    # Criando um filtro de dados para dia e hora de recebimento do exame
    dh_recebimento_exame = st.selectbox('Selecione o dia e horário do recebimento do exame: ', ['Todos'] + list(arquivo['dh_recebimento_exame'].unique()))

    if dh_recebimento_exame != 'Todos':

        arquivo_filt = arquivo_filt[arquivo_filt['dh_recebimento_exame'] == dh_recebimento_exame]

    # Criando um filtro de dados para o tipo de bactéria
    ds_micro_organismo = st.selectbox('Selecione o tipo de bactéria: ', ['Todos'] + list(arquivo['ds_micro_organismo'].unique()))

    if ds_micro_organismo != 'Todos':

        arquivo_filt = arquivo_filt[arquivo_filt['ds_micro_organismo'] == ds_micro_organismo]

    # Criando um filtro de dados para o tipo de antibiótico utilizado
    ds_antibiotico_microorganismo = st.selectbox('Selecione o tipo de antibiótico utilizado: ', ['Todos'] + list(arquivo['ds_antibiotico_microorganismo'].unique()))

    if ds_antibiotico_microorganismo != 'Todos':

        arquivo_filt = arquivo_filt[arquivo_filt['ds_antibiotico_microorganismo'] == ds_antibiotico_microorganismo]

    # Criando um filtro de dados para a interpretação do antibiograma
    cd_interpretacao_antibiograma = st.selectbox('Selecione o resultado da interpretação do antibiograma: ', ['Todos'] + list(arquivo['cd_interpretacao_antibiograma'].unique()))

    if cd_interpretacao_antibiograma != 'Todos':

        arquivo_filt = arquivo_filt[arquivo_filt['cd_interpretacao_antibiograma'] == cd_interpretacao_antibiograma]

    # Criando um filtro de dados para o local de coleta
    ds_unidade_coleta = st.selectbox('Selecione o local de coleta: ', ['Todos'] + list(arquivo['ds_unidade_coleta'].unique()))

    if ds_unidade_coleta != 'Todos':

        arquivo_filt = arquivo_filt[arquivo_filt['ds_unidade_coleta'] == ds_unidade_coleta]

    # Mostrando a tabela na tela do usuário
    st.dataframe(arquivo_filt)

else:

        st.subheader('Não há dados disponíveis')