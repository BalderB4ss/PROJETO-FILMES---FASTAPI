import streamlit as st
import requests

# URL da API FastAPI
API_URl = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Filmes", page_icon="🎥")
st.title("🎬 Gerenciador de Filmes")

# Menu lateral
menu = st.sidebar.radio("Navegação", ["Catálogo","Adicionar filme"])

if menu == "Catálogo":
    st.subheader("Todos os filmes disponíveis")
    response = requests.get(f"{API_URl}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            # for filme in filmes:
            #     st.write(f"**{filme['titulo']} | {filme['genero']} | {filme['ano']} | {filme['avaliacao']}** ")          Jeito mais feio
            tabela_filmes = {
                "titulo": [filme['titulo'] for filme in filmes[0]],
            }
        else:
            st.warning("Não há nenhum filme cadastrado!")
    else:
        st.error("Erro ao acessar a API❗")