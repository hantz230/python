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
                email      VARCHAR(100),
                telefone     VARCHAR(11),
            )
        """)

        conexao.commit()
        print("Tabela criada com sucesso!")

    except mysql.connector.Error as erro:
        print(f"Erro: {erro}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def cadastrar_cliente( nome, email, telefone):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, email, telefone) VALUES (%s, %s, %s)",
            (nome, email, telefone)
        )
        conexao.commit()
        print(f"Produto '{nome}' cadastrado.")
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
        for p in cursor.fetchall():
            print(f"{p[0]} | {p[1]} | {p[2]} | {p[3]}")
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
        for p in cursor.fetchall():
            print(f"{p[0]} | {p[1]} | {p[2]} | {p[3]}")
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
            "UPDATE cliente SET email = %s WHERE id = %s",
            (novo_email, id_cliente)
        )
        conexao.commit()
        if cursor.rowcount > 0:
            print("Email atualizado com sucesso.")
        else:
            print(f"Cliente com id {id_cliente} não encontrado.")
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
        cursor.execute("SELECT nome FROM clientes WHERE id = %s", (id_cliente,))
        cliente = cursor.fetchone()
        if not cliente:
            print(f"cliente com id {id_cliente} não encontrado.")
            return
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
        conexao.commit()
        print(f"cliente '{cliente[0]}' excluído com sucesso.")
    except mysql.connector.Error as erro:
        print(f"Erro ao excluir: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()


# --- Uso ---
def menu():
    while True:
        print("\n===== SISTEMA DE CLIENTES =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Buscar cliente")
        print("4 - Atualizar email")
        print("5 - Excluir cliente")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("email: ")
            telefone = input("telefone: ")
            cadastrar_cliente(nome, email, telefone)
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            termo = input("Buscar por nome: ")
            buscar_cliente(termo)
        elif opcao == "4":
            pid = int(input("ID do produto: "))
            novo = input("Novo email: ")
            atualizar_email(pid, novo)
        elif opcao == "5":
            pid = int(input("ID do produto: "))
            excluir_cliente(pid)
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

#--- Chamado das funções ---
criar_tabela()          #executar uma unica vez

menu()                   #executa de modo recorrente