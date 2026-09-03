class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir(self):
        print(f"Nome: {self.nome} | Email: {self.email} | Telefone: {self.telefone}")

    def converte_tupla(self):
        return (self.nome, self.email, self.telefone)

    @staticmethod
    def reverte_tupla(tupla):
        cliente = Cliente(
            nome=tupla[1],
            email=tupla[2],
            telefone=tupla[3]
        )
        cliente.id = tupla[0]
        return cliente
