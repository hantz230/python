class Animal:
    def __init__(self, nome):
        self.nome = nome
    def emitir_som(self):
        print(self.nome+" emiti um som generico ")

class Cachorro(Animal):
    def emitir_som(self):
        print(self.nome+" late: Au Au!")

class Gato(Animal):
    def emitir_som(self):
        print(self.nome+" mia: Miau!")

def fazer_barulho(animal):
    animal.emitir_som()

animais = [Cachorro("Rex"), Gato("Mimi"), Animal("Animal Generico")]
for animal in animais:
    fazer_barulho(animal)