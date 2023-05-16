# pip install streamlit pandas matplotlib seaborn
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fonte de Dados
# https://www.kaggle.com/datasets/whenamancodes/student-performance

# Especificando o título da página e o ícone
st.set_page_config(page_title="Dashboard - Student Dataset", page_icon=":books:")

# sidebar
st.sidebar.title("Configurações de Exibição")

# Carregando o dataset
show_id = "1378939680"

gsheets_url = 'https://docs.google.com/spreadsheets/d/1Xr6uPNAlT4n9FDuR91JyY2QwFGLGmMICPE5WqjW-s1k/export?format=csv&gid=' + show_id

data = pd.read_csv(gsheets_url, on_bad_lines='skip')

st.dataframe(data)


# Adicionando um gráfico de barras para mostrar o quantidade de compareceu por Refeicao
st.title("Quantidade de alunos por Refeicao")
fig, ax = plt.subplots()
ax = sns.countplot(x="Refeicao", hue="Compareceu", data=data)
st.pyplot(fig)

#adicionar um grafico de linhas para mostrar a quantidade de quem nao compareceu por Refeicao
st.title("Quantidade de alunos que não compareceram por Refeicao")
fig, ax = plt.subplots()
ax = sns.countplot(x="Refeicao", hue="Compareceu", data=data[data["Compareceu"] == "Não"])
st.pyplot(fig)
