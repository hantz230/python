agenda = {}


while True:
    print("\n1- Cadastrar")
    print("2- Consultar")
    print("3- Consultar toda a lista")
    print("4- Sair")

    opcao = input("opcao: ")

    if opcao == "1":
        nome = input("Nome: ")
        if nome in agenda:
            print("nome ja cadastrado")
        else:
            while True:
                telefone = input("Telefone: ")
                if telefone != "":
                    break
                else:
                    print("telefone obrigatorio")
            agenda[nome] = telefone
            print("contato cadastrado")
    elif opcao == "2":
        nome = input("Nome: ")
        if nome in agenda:
            print(f"Telefone de {nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado")
    elif opcao == "3":
        if agenda:
            print("Lista de contatos:")
            for nome, telefone in agenda.items():
                print(f"{nome}: {telefone} , Id - {list(agenda.keys()).index(nome)+1}")
        else:
            print("Agenda vazia")
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida")