import streamlit as st
import pandas as pd

# Carregar os dados
data = pd.read_excel('BASE_DE_TESTE.xlsx', sheet_name='Planilha1')

# Título do Dashboard
st.title('Dashboard de Projetos')

# Subtítulo
st.subheader('Visualização de dados de câmeras e evolução de projetos')

# Filtro por região
regioes = data['REGIÃO'].unique()
regiao_selecionada = st.sidebar.selectbox('Selecione a Região', regioes)

# Filtrar dados pela região selecionada
dados_filtrados = data[data['REGIÃO'] == regiao_selecionada]

# Mostrar a tabela de dados filtrados
st.write(f"Dados filtrados pela região: {regiao_selecionada}")
st.dataframe(dados_filtrados)

# Gráfico de Barras: Quantidade de Câmeras Internas por Cidade
st.bar_chart(dados_filtrados.groupby('CIDADE')['Qtd. Câmeras Internas'].sum())

# Gráfico de Linhas: Evolução dos Projetos por Cidade
st.line_chart(dados_filtrados.groupby('CIDADE')['% EVOLUÇÃO'].mean())

# Mostrar um resumo dos dados
st.write("Resumo dos Dados Filtrados:")
st.write(dados_filtrados.describe())
