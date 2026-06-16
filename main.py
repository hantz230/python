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

'''

# calculadora

idade= int(input("digite sua idade: "))

print("a sua idade daqui a 5 anos será : ", idade + 5 )