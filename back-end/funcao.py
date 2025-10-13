from conexao import conectar
def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
CREATE TABLE IF NOT EXISTS filmes (
id SERIAL PRIMARY KEY,
titulo TEXT NOT NULL,
genero TEXT NOT NULL,
ano INTEGER NOT NULL,
avaliacao REAL
)
""")
            conexao.commit()
        except Exception as error:
            print(f"Erro ao criar tabela: {error}")
        finally:
            cursor.close()
            conexao.close()

def inserir_filme(titulo, genero, ano, avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("INSERT INTO filmes (titulo, genero, ano, avaliacao) VALUES (%s, %s, %s, %s)",
                           (titulo, genero, ano, avaliacao))
            conexao.commit()
        except Exception as error:
            print(f"Erro ao inserir filme: {error}")
        finally:
            cursor.close()
            conexao.close()

def listar_filmes():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("SELECT * FROM filmes ORDER BY id")
            return cursor.fetchall()
        except Exception as error:
            print(f"Erro ao tentar listar filmes: {error}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_filme(id_filme,novo_titulo,novo_genero,novo_ano,nova_avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("UPDATE filmes SET titulo = %s, genero = %s, ano = %s, avaliacao = %s WHERE id = %s",
                           (novo_titulo,novo_genero,novo_ano,nova_avaliacao,id_filme))
            conexao.commit()
        except Exception as error:
            print(f"Erro ao tentar atualizar filme: {error}")
        finally:
            cursor.close()
            conexao.close()
def deletar_filme(id_filme):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("DELETE FROM filmes WHERE id = %s",(id_filme,))
            conexao.commit()
        except Exception as error:
            print(f"Erro ao tentar deletar filme: {error}")
        finally:
            cursor.close()
            conexao.close()
