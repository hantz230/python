class Produto:
    def __init__(self, nome, preco, quantidade):

        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

        Produto.total_cadastrado+=1

    def valor_em_estoque(self):
        return self.preco * self.quantidade

    def aplicar_desconto(self, percentual):
        if 0< percentual < 100:
            self.preco -= self.preco * (percentual/100)
        else:
            print("percentual de desconto invalido")
    def info(self):
        print(f"produto: {self.nome} \npreco: {self.preco:.2f} \nquantidade: {self.quantidade} \ntotal: {self.valor_em_estoque():.2f} \n")

    @classmethod
    def exibir_cadastros(cls):
            print(f"Total de produtos cadastrados: {cls.total_cadastrado}")

    #uso da classe
p1=Produto("notebook", 100, 100)

p2=Produto("aanaf", 10430, 10)

p1.info()

p2.aplicar_desconto(15)
p2.info()