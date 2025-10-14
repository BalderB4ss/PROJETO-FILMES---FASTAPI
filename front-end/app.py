import streamlit as st
import requests

# URL da API FastAPI
API_URl = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Filmes", page_icon="🎥")
st.title("🎬 Gerenciador de Filmes")

# Menu lateral
menu = st.sidebar.radio("Navegação", ["Catálogo","Adicionar Filme","Apagar Filme","Atualizar Filme"])

if menu == "Catálogo":
    st.subheader("Todos os filmes disponíveis")
    response = requests.get(f"{API_URl}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            # for filme in filmes:
            #     st.write(f"**{filme['titulo']} | {filme['genero']} | {filme['ano']} | {filme['avaliacao']}** ")          Jeito mais feio
            tabela_filmes = {
                "id": [filme['id'] for filme in filmes],
                "titulo": [filme['titulo'] for filme in filmes],
                "genero": [filme['genero'] for filme in filmes],
                "ano": [filme['ano'] for filme in filmes],
                "avaliacao": [f"{filme['avaliacao']:,.1f}" for filme in filmes],
            }
            st.table(tabela_filmes)
        else:
            st.warning("Não há nenhum filme cadastrado!")
    else:
        st.error("Erro ao acessar a API❗")

elif menu == "Adicionar Filme":
    st.subheader("➕ Adicionar Filme ➕")
    titulo = st.text_input("Título do filme")
    genero = st.text_input("Gênero")
    ano = st.number_input("Ano de Lançamento", min_value=1887, max_value=2030, step=1)
    avaliacao = st.number_input("Avaliação de (0 à 10)", min_value=0.0, max_value=10.0, step=0.1)
    if st.button("Adicionar"):
        dados = {"titulo": titulo, "genero": genero, "ano":ano, "avaliacao":avaliacao}
        response = requests.post(f"{API_URl}/filmes", params=dados)
        if response.status_code == 200:
            st.success("Filme adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar o filme❗")