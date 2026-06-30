class ContaBancaria:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    # depositar
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"{valor} depositado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    #SACAR
    def sacar(self, valor):
        if valor <= 0:
            print("valor de saque invalido ")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"{valor} sacado com sucesso.")

    #fazer extrato
    def extrato(self):
        print("=" * 30)
        print(f"Titular: {self.titular}")
        print(f"Número da conta: {self.numero}")
        print(f"Saldo atual: {self.saldo}")
        print("=" * 30)

conta1 = ContaBancaria("Ramos", "001-2", 500.00)
conta1.depositar(100)
conta1.extrato()
conta1.sacar(100)
conta1.extrato()

conta2 = ContaBancaria("pia", "0987", 20000.00)
conta2.extrato()
conta2.depositar(123400)
conta2.extrato()
conta2.sacar(10000)
conta2.extrato()