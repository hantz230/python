# ==================================================================================

#                       Estrutura basica das funções

#_____________________________________________
# função If else

  #  if valor1 > valor2:
   #     print("valor1 é maior que valor2")
  #  else:
   #     print("valor2 é maior que valor1")

#_____________________________________________
# função For

#Array = ["valor1", "valor2", "valor3"]

#for item in Array:

 #   print(item)
#__________________________________________________________________
#função while e switch case

#def exibir_menu():
#    while True:
#        print("\n--- MENU PRINCIPAL ---")
 #       print("1. Cadastrar usuário")
 #       print("2. Listar dados")
#        print("3. Configurações")
 #       print("0. Sair")

#        opcao = input("Escolha uma opção: ")

 #       match opcao:
 #           case "1":
 #               print("-> Executando: Cadastro de usuário...")
 #           case "2":
 #               print("-> Executando: Listagem de dados...")
#            case "3":
#                print("-> Executando: Abrindo configurações...")
#            case "0":
 #               print("Saindo do sistema. Até logo!")
 #               break  # Quebra o laço 'while' e encerra a função
 #           case _:
 #               print("Opção inválida! Tente novamente.")


# Executa a função
#exibir_menu()

#====================================================================================
'''
#tipo de dados

idade = 18
altura = 1.75
nome = "João"

aprovado = True

frutas = ["maçã", "banana","uva"]

cores = ("azul", "verde","vermelho")

aluno = {
    "nome": "Maria ",
    "idade":18,
    "curso": "desenvolvimento de Sistema"
}

print("Exemplos  de tipos de dados em Python\n")

print("idade = ", idade)
print("tipo : ",type(idade))

print("\naltura = ", altura)
print("tipo : ",type(altura))

print("\nnome = ", nome)
print("tipo : ",type(nome))

print("\naprovado = ", aprovado)
print("tipo : ",type(aprovado))

print("\nfrutas = ", frutas)
print("tipo : ",type(frutas))

print("\ncores = ", cores)
print("tipo : ",type(cores))

print("\naluno = ", aluno)
print("tipo : ",type(aluno))


print("digite seu nome:")
nomeUser = input()

#usuario

idadeUser = int(input("digite sua idade: "))

print("Quantidade em dinheio ")
dinheiro = float(input())

Usuario = {nomeUser,idadeUser,dinheiro}

print("seu usuario: ", Usuario  )

print(f"seu usuario: {Usuario}")

#item

item= input("digite o item: ")

quantidade = int(input("digite quantidade: "))

preco = float(input("digite preço: "))

print(f"item: {item}, quantidade: {quantidade}, preco: {preco}")



# calculadora

idade= int(input("digite sua idade: "))

print("a sua idade daqui a 5 anos será : ", idade + 5 )



#exemplo Lista
alunos = ["ana","joao","Maria"]
alunos.append("pedro")
alunos.remove("joao")

print(alunos)



# exemplo de tupla

meses = ("janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro")

print(meses[4])

'''