import mysql.connector
from config import DB_CONFIG
from banco import criar_tabela
import banco
import clientes
from models import Cliente

def exibir_lista(lista):
    if lista:
        for cliente in lista:
            cliente.exibir()
    else:
        print("Nenhum cliente encontrado.")

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
            email = input("Email: ")
            telefone = input("Telefone: ")

            novo_cliente = Cliente(nome, email, telefone)
            clientes.cadastrar_cliente(novo_cliente)


        elif opcao == "2":
            exibir_lista(clientes.listar_clientes())

        elif opcao == "3":
            termo = input("Buscar por nome: ")

            exibir_lista(clientes.buscar_cliente(termo))

        elif opcao == "4":
            cid = int(input("ID do cliente: "))
            novo_email = input("Novo email: ")

            clientes.atualizar_email(cid, novo_email)

        elif opcao == "5":
            cid = int(input("ID do cliente: "))
           
            clientes.excluir_cliente(cid)

        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
