class carro:
    def __init__(self, marca, modelo,ano, velocidade=0 ):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade


    def acelerar(self, valor):
        if valor > 0:
            self.velocidade += valor
            print(f"o carro acelerou {valor} km/h")
        else:
            print("valor de aceleração invalido")

    def frear(self, valor):
        if valor > 0:
            if self.velocidade - valor <= 0:
                print("o carro não pode parar")
            else:
                self.velocidade -= valor
                print(f"o carro freou {valor} km/h")
        else:
            print("valor de frenagem invalido")

    def exibir_info(self):
        print("="*30)
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Velocidade atual: {self.velocidade} km/h")
        print("="*30)

Carro1 = carro("Fiat", "uno", 2018, 100)
Carro1.exibir_info()
Carro1.acelerar(10)
Carro1.frear(50)
Carro1.exibir_info()
