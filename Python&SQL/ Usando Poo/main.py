import mysql.connector
from config import DB_CONFIG
from banco import criar_tabela
import produtos

# --- Uso ---
def menu():
    while True:
        print("\n===== SISTEMA DE PRODUTOS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Atualizar preço")
        print("5 - Excluir produto")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            qtd = int(input("Quantidade: "))
            cat = input("Categoria: ")
            produtos.cadastrar_produto(nome, preco, qtd, cat)
        elif opcao == "2":
            produtos.listar_produtos()
        elif opcao == "3":
            termo = input("Buscar por nome: ")
            produtos.buscar_produto(termo)
        elif opcao == "4":
            pid = int(input("ID do produto: "))
            novo = float(input("Novo preço: "))
            produtos.atualizar_preco(pid, novo)
        elif opcao == "5":
            pid = int(input("ID do produto: "))
            produtos.excluir_produto(pid)
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

#--- Chamado das funções ---

menu()                   #executa de modo recorrente