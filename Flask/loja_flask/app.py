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

@app.route("/categoria/<nome>")
def categoria(nome):
    return render_template("categoria.html", nome=nome)

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

#Inicia o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)