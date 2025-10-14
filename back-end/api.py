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
    return {"mensagem": "Bem-vindo ao Gerenciador de Filmes"}

@app.post("/filmes")
def criar_filmes(titulo:str, genero:str, ano:int, avaliacao:float):
    inserir_filme(titulo, genero, ano, avaliacao)
    return {"mensagem": "Filme adicionado com sucesso!"}

@app.get("/filmes")
def exibir_filmes():
    filmes = listar_filmes()
    lista = []
    for filme in filmes:
        lista.append({
            "id": filme[0],
            "titulo": filme[1],
            "genero": filme[2],
            "ano": filme[3],
            "avaliacao":filme[4]})
    return {"filmes": lista}

@app.delete("/filmes")
def apagar_filme(id:int):
    deletar_filme(id)
    return {"Mensagem": "Filme deletado com sucesso"}