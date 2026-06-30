agenda = {}


while True:
    print("\n1- Cadastrar")
    print("2- Consultar")
    print("3- Consultar toda a lista")
    print("4- Consultar por letra")
    print("5- excluir")
    print("6- Sair")

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
         letra = input("Digite a letra inicial: ").upper()
         contatos_encontrados = []
         for nome, telefone in agenda.items():
             if nome.startswith(letra):
                 contatos_encontrados.append((nome, telefone))
         if contatos_encontrados:
             print("Contatos encontrados:")
             for nome, telefone in contatos_encontrados:
                 print(f"{nome}: {telefone} , Id - {list(agenda.keys()).index(nome) + 1}")
         else:
             print("Nenhum contato encontrado com essa letra inicial.")
    elif opcao == "5":
        nome = input("Nome: ")
        if nome in agenda:
            del agenda[nome]
            print("Contato excluído")
        else:
            print("Contato não encontrado")
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida")