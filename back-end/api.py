from fastapi import FastAPI
from funcao import atualizar_filme, deletar_filme, inserir_filme, listar_filmes

# Rodar o fastapi
# python -m uvicorn api:app --reload

# Testar api FASTAPI
# /doc > Documentação Swagger
# /redoc > Documentação redoc


# Iniciar o fastapi 
app = FastAPI(title="Gerenciador de Filmes")

# GET = pegar / listar
# POST = Criar / Enviar
# PUT = Aualizar
# DELETE = Deletar

@app.get("/")
def home():
    return {"mensagem": "Quero café prof"}

@app.post("/filmes")
def criar_filmes(titulo:str, genero:str, ano:int, avaliacao:float):
    inserir_filme(titulo, genero, ano, avaliacao)
    return {"mensagem": "Filme adicionado com sucesso!"}