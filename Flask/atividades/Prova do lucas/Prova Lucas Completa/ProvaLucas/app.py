from flask import Flask
from flask import Flask, render_template
#Cria a aplicação Flask
app = Flask(__name__)

#Define uma rota
#@app.route("/")
#def index():
    #return "Olá, mundo! O Flask OK."

lista=[
        {"id": 1, "nome":"X Burguer", "preco": 35.99, "tipo":"Lanche", "disponivel": True},
        {"id": 2, "nome":"Pudim", "preco": 9.25, "tipo":"Sobremesa", "disponivel": False},
        {"id": 3, "nome":"Batata Frita", "preco": 15.99, "tipo":"Lanche", "disponivel": True},
        {"id": 4, "nome":"Taça de sorvete", "preco": 12.89, "tipo":"Sobremesa", "disponivel": False},
        {"id": 5, "nome":"Coca Cola", "preco": 9.99, "tipo":"Bebida", "disponivel": True},
        {"id": 6, "nome":"X Salada", "preco": 15.99, "tipo":"Lanche", "disponivel": True},
        {"id": 7, "nome":"Pudim Chocolate", "preco": 35.99, "tipo":"Sobremesa", "disponivel": True}

    ]

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/item/<int:id>")
def detalhe_produto(id):
    item= None
    for i in lista:
        if i["id"] == id:
            item = i
            break
    return render_template("detalhe.html", id=id, item=item)


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/produtos")
def produtos():
    return render_template("catalogo.html", item=lista)
@app.route("/cardapio")
def catalogo():
    return render_template("cardapio.html", item=lista)


#Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)