import mysql.connector
from config import DB_CONFIG
from banco import *
import models

def cadastrar_produto(nome, preco, tipo, disponivel):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO cardapio (nome, preco, tipo, disponivel) VALUES (%s, %s, %s, %s)",
            (nome, preco, tipo, disponivel)
        )
        conexao.commit()
        print(f"Item '{nome}' cadastrado.")
    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def listar_produtos():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM cardapio ORDER BY nome")
        for p in cursor.fetchall():
            print(f"{p[0]} | {p[1]} | Preco: {p[2]} | Tipo: {p[3]} | Disponivel: {p[4]}")
    except mysql.connector.Error as erro:
        print(f"Erro ao listar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def buscar_produto(termo):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT * FROM cardapio WHERE nome LIKE %s ORDER BY nome",
            (f"%{termo}%",)
        )
        for p in cursor.fetchall():
            print(f"{p[0]} | {p[1]} | Preco: {p[2]} | Tipo: {p[3]} | Disponivel: {p[4]}")
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def excluir_produto(id):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT nome FROM cardapio WHERE id = %s", (id))
        item = cursor.fetchone()
        if not item:
            print(f"Produto com id {id} não encontrado.")
            return
        cursor.execute("DELETE FROM produtos WHERE id = %s", (id))
        conexao.commit()
        print(f"Produto '{item[0]}' excluído com sucesso.")
    except mysql.connector.Error as erro:
        print(f"Erro ao excluir: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()