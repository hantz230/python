class calculadora:
    historico = []
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def soma (self):
        self.historico.append(f"soma: {self.A} - {self.B} = {self.A + self.B}")
        return (self.A + self.B)

    def subtracao(self):
        self.historico.append(f"Subtração: {self.A} - {self.B} = {self.A - self.B}")
        return (self.A - self.B)

    def multiplicacao(self):
        self.historico.append(f"Multiplicação: {self.A} * {self.B} = {self.A * self.B}")
        return (self.A * self.B)

    def divisao(self):
        if self.B != 0:
            self.historico.append(f"Divisão: {self.A} / {self.B} = {self.A / self.B}")
            return (self.A / self.B)
        else:
            self.historico.append(f"Divisão: {self.A} / {self.B} = Erro: Divisão por zero")
            return "Erro: Divisão por zero"

    def exibir_historico(self):
        print("Histórico de operações:")
        for operacao in self.historico:
            print(operacao)


calculadora1 = calculadora(100, 25)
calculadora1.soma()
calculadora1.subtracao()
calculadora1.multiplicacao()
calculadora1.divisao()
calculadora1.exibir_historico()