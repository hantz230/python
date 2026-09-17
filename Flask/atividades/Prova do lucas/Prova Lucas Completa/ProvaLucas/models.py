import mysql.connector
from config import DB_CONFIG
from banco import *
import models

class Item:
    def __init__(self, nome, preco, tipo, disponivel):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
        self.disponivel = disponivel

    def converte_tupla(self):
        return (self.nome, self.preco, self.tipo, self.disponivel)

    @staticmethod
    def reverte_tupla(tupla):
        item = Item(
            nome=tupla[1],
            preco=tupla[2],
            tipo=tupla[3],
            disponivel=tupla[4]


        )
        Item.id = tupla[0]
        return item


    def exibir(self):
        print(f"{self.nome} | R$: {self.preco} | Tipo: {self.tipo}|Disponibilidade: {self.disponivel}")

p1= Item("X Burguer", 30.99, "Lanche", True )

p2= Item("Pudim", 9.25, "Sobremesa", True )

p3 = Item.reverte_tupla((3, "Milkshake de Creme", 14.90, "Bebida", False))

p1.exibir()
p2.exibir()
p3.exibir()
