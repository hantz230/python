# cria a aplicação Flask
from flask import Flask, render_template
app = Flask(__name__)

#define a rota principal
@app.route("/")

def index():
    return render_template("index.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/produto/<int:id>")
def produto(id):
    return render_template("produto.html", id=id)

@app.route("/produtos")
def produtos():
    lista = [
        {"nome": "brouwne", "preco": 20.00,"categoria": "doce"},
        {"nome": "Morango do amor", "preco": 16.99,"categoria": "doce"},
        {"nome": "milk shake", "preco": 10.00,"categoria": "bebida"},
        {"nome": "Bolo de cenora", "preco": 10.00, "categoria": "doce"},
        {"nome": "American coffee", "preco": 08.00, "categoria": "bebida"},
    ]
    return render_template("produtos.html", produtos=lista)

#Inicia o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)