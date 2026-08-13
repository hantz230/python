import mysql.connector
from config import DB_CONFIG

def relatorio():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("select count(*) from produtos")
        for p in cursor.fetchall():
            print(f"{p[0]}")
    except mysql.connector.Error as erro:
        print(f"Erro ao listar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def relatorio_total():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("select sum(preco*quantidade) from produtos")
        for p in cursor.fetchall():
            print(f"{p[0]}")
    except mysql.connector.Error as erro:
        print(f"Erro ao listar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def produto_mais_caro():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("select max(preco) from produtos;")
        for p in cursor.fetchall():
            print(f"{p[0]}")
    except mysql.connector.Error as erro:
        print(f"Erro ao listar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

relatorio()
relatorio_total()
produto_mais_caro()

