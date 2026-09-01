# cria a aplicação Flask
from flask import Flask, render_template
app = Flask(__name__)

lista = [
    {"id": 1, "nome": "brouwne", "preco": 20.00, "categoria": "doce", "quantidade": 10},
    {"id": 2, "nome": "Morango do amor", "preco": 16.99, "categoria": "doce", "quantidade": 5},
    {"id": 3, "nome": "milk shake", "preco": 10.00, "categoria": "bebida", "quantidade": 8},
    {"id": 4, "nome": "Bolo de cenora", "preco": 10.00, "categoria": "doce", "quantidade": 3},
    {"id": 5, "nome": "American coffee", "preco": 08.00, "categoria": "bebida", "quantidade": 12},
    {"id": 6, "nome": "Capuccino", "preco": 12.00, "categoria": "bebida", "quantidade": 0}
]
#define a rota principal
@app.route("/")

def index():
    return render_template("index.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/produto/<int:id>")
def detalhe_produto(id):
    produto = None

    for p in lista:
        if p["id"] == id:
            produto = p
            break
    return render_template("detalhe.html", id=id, produto=produto)

@app.route("/produtos")
def produtos():

    return render_template("produtos.html", produtos=lista)

@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html", produtos=lista)

@app.route("/categoria/<nome>")
def categoria(nome):
    produtos_filtrados = [produto for produto in lista if produto["categoria"] == nome]
    return render_template("catalogo.html", produtos=produtos_filtrados)

#Inicia o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)