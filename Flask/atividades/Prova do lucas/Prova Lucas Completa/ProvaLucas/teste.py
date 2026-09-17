import mysql.connector
from config import DB_CONFIG
from banco import criar_tabela
import models
from models import Item
import cardapio
import banco
import cardapio


# --- Uso ---
def exibir_lista(lista):
    if lista:
        for item in lista:
            item.exibir()
    else:
        print("Item não encontrado!")
def menu():
    while True:
        print("\n===== SISTEMA DE ITENS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            tipo = input("Tipo: ")
            disponivel = bool(input("Disponivel: "))
            novo_item = Item(nome, preco, tipo, disponivel)
            cardapio.cadastrar_produto(nome, preco, tipo, disponivel)
        elif opcao == "2":
            exibir_lista(cardapio.listar_produtos())
        elif opcao == "3":
            termo = input("Buscar por nome: ")
            exibir_lista(cardapio.buscar_produto(termo))
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

#--- Chamado das funções ---

menu()                   #executa de modo recorrente