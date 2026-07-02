class pessoa:
    def __init__(self, nome, idade , cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade



    def apresentar(self):
        print("="*30)
        print(f"Ola, meu Nome é : {self.nome} , tenho {self.idade} anos e moro em  {self.cidade})")
        print("=" * 30)

pessoa1 = pessoa("Aana", 15 , "sheresd")
pessoa1.apresentar()

pessoa2 = pessoa("marcio", 1 , "USA")
pessoa2.apresentar()