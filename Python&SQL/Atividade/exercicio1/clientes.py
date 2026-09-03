import mysql.connector
from config import DB_CONFIG
from models import Cliente
import banco

def cadastrar_cliente(cliente: Cliente):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)",
            cliente.converte_tupla()
        )
        conexao.commit()
        print(f"Cliente {cliente.nome} cadastrado.")
    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()
def listar_clientes():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM clientes ORDER BY nome")
        return [Cliente.reverte_tupla(linha) for linha in cursor.fetchall()]
    except mysql.connector.Error as erro:
        print(f"Erro ao listar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def buscar_cliente(termo):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT * FROM clientes WHERE nome LIKE %s ORDER BY nome",
            (f"%{termo}%",)
        )
        return [Cliente.reverte_tupla(linha) for linha in cursor.fetchall()]
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def atualizar_email(id_cliente, novo_email):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE clientes SET email = %s WHERE id = %s",
            (novo_email, id_cliente)
        )
        conexao.commit()
        if cursor.rowcount > 0:
            print(f"Email do cliente {id_cliente} atualizado.")
        else:
            print(f"Email do cliente {id_cliente} não encontrado.")
    except mysql.connector.Error as erro:
        print(f"Erro ao atualizar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()
def excluir_cliente(id_cliente):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT * FROM clientes WHERE id = %s",
            (id_cliente,)
        )
        cliente = cursor.fetchone()
        if not cliente:
            print(f"Cliente com id {id_cliente} não encontrado.")
            return
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
        conexao.commit()
        print(f"Cliente {id_cliente} excluído.")

    except mysql.connector.Error as erro:
        print(f"Erro ao excluir: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()