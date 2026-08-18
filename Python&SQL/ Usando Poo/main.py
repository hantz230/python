import mysql.connector
from config import DB_CONFIG
from banco import criar_tabela
import banco
import relatorio
import produtos
from models import Produto

# --- Uso ---
def exibir_lista(lista):
    if lista:
        for produto in lista:
            produto.exibir()
    else:
        print("Nenhum produto encontrado.")
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

            novo_produto = Produto(nome, preco, qtd, cat)
            produtos.cadastrar_produto(novo_produto)

        elif opcao == "2":
            exibir_lista(produtos.listar_produtos())
        elif opcao == "3":
            termo = input("Buscar por nome: ")
            exibir_lista(produtos.buscar_produto(termo))
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
#banco.criar_tabela()
menu()                   #executa de modo recorrente