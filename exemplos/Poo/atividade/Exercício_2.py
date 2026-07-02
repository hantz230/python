class Retangulo :
    def __init__(self, Largura, Altura):
        self.Largura = Largura
        self.Altura = Altura

    def area(self):
        print(f"A area do retangulo é : {self.Largura * self.Altura}")
        return self.Largura * self.Altura
    def perimetro(self):
        print(f"o perimetro do retangulo é : {(self.Largura+self.Altura) * 2}")
        return (self.Largura+self.Altura) * 2
    def exibir_info(self):
        print(f"informações do retangulo:")
        self.area()
        self.perimetro()
retangulo1 = Retangulo( 10 , 5)
retangulo1.area()
retangulo1.perimetro()
retangulo1.exibir_info()

retangulo2 = Retangulo( 100 , 100)
retangulo2.area()
retangulo2.perimetro()
retangulo2.exibir_info()
