import mysql.connector
from config import DB_CONFIG

def criar_tabela():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id         INT           AUTO_INCREMENT PRIMARY KEY,
                nome       VARCHAR(100)  NOT NULL,
                email      VARCHAR(100)  NOT NULL,
                telefone   VARCHAR(15)   NOT NULL
            )
        """)

        conexao.commit()
        print("Tabela criada com sucesso!")

    except mysql.connector.Error as erro:
        print(f"Erro: {erro}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()

criar_tabela()