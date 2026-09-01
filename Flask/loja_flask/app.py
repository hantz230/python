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
    return render_template("produto.html")

@app.route("/categoria/<nome>")
def categoria(nome):
    return render_template("categoria.html")

@app.route("/produtos")
def produtos():
    lista = [
        {"nome": "Notebook", "preco": 3499.00,"categoria": "Eletronicos"},
        {"nome": "Mouse", "preco": 89.00,"categoria": "Eletronicos"},
        {"nome": "Teclado", "preco": 249.00,"categoria": "Eletronicos"},
    ]
    return render_template("produtos.html", produtos=lista)

#Inicia o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)