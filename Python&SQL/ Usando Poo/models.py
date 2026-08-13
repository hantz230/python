class Produto:
    def __init__(self, nome, preco, quantidade, categoria):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria

    def converte_tupla(self):
        return (self.nome, self.preco, self.quantidade, self.categoria)

    @staticmethod
    def reverte_tupla(tupla):
        produto = Produto(
            nome=tupla[1],
            preco=tupla[2],
            quantidade=tupla[3],
            categoria=tupla[4]
        )
        produto.id = tupla[0]
        return produto

    def exibir(self):
        print(f"{self.id} | {self.nome} | R${self.preco:.2f} | Qtd: {self.quantidade} | {self.categoria}")