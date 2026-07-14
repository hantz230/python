class Forma:
    def __init__(self, nome = "Forma generica"):
        self.nome = nome

    def calcular_area(self):
        return 0
    def descricao(self):
        return self.nome

class circulo(Forma):
    def __init__(self, raio):
        super().__init__("Circulo")
        self.raio = raio

    def calcular_area(self):
        return 3.1415 * self.raio ** 2

    def descricao(self):
        return f"{self.nome} de raio {self.raio}"

class Retangulo(Forma):
    def __init__(self, largura, altura):
        super().__init__("Retangulo")
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def descricao(self):
        return f"{self.nome} de dimensões {self.largura} x {self.altura}"

def exibir_areas(forma):
    print(f"{forma.descricao()} - Area ; {forma.calcular_area()}")
formas = [circulo(5), Retangulo(4, 6), circulo(7), Retangulo(8, 9)]

for forma in formas:
    exibir_areas(forma)