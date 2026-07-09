class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print(f"{self.nome} emite um som")

    def mover(self):
        print(f"{self.nome} se move de alguma forma")

    def exibir_info(self):
        print(f"Animal {self.nome} | Idade: {self.idade} anos ")

class Cachorro (Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        print(f"{self.nome} late: Au Au!")

    def mover(self):
        print(f"{self.nome} corre em quatro patas")

    def exibir_info(self):
        super().exibir_info()
        print(f"Raça: {self.raca}")

class Passaro(Animal):
    def __init__(self, nome, idade, pode_voar):
        super().__init__(nome, idade)
        self.pode_voar = pode_voar

    def emitir_som(self):
        print(f"{self.nome} canta: Piu piu!")

    def mover(self):
        if self.pode_voar:
            print(f"{self.nome} voa com asas")
        else:
            print(f"{self.nome} anda com patas")

    def exibir_info(self):
        super().exibir_info()
        print(f"Pode voar: {'sim' if self.pode_voar else 'não'}")

#uso

c= Cachorro("tobi",3 , "Labrador")
p1= Passaro("Azul",6,True)
p2= Passaro("Pinguim",5,False)

c.emitir_som()
c.exibir_info()
c.mover()

p1.emitir_som()
p1.exibir_info()
p1.mover()

p2.emitir_som()
p2.exibir_info()
p2.mover()