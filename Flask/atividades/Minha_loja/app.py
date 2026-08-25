# cria a aplicação Flask
from flask import Flask
app = Flask(__name__)

#define a rota principal
@app.route("/")

def index():
    return "olá, mundo! o flask está funcionando"

@app.route("/sobre")
def sobre():
    return "esta é a página sfsfsobre."

@app.route("/produto/<int:id>")
def produto(id):
    return f"Produto com id: {id}"

@app.route("/produtos")
def produtos():
    return (
            "Esta é a página de produtos."
    "Aqui você pode encontrar uma lista de produtos disponíveis."
            "1- Produto A"
            "2- Produto B" 
            "3- Produto C"
)




#Inicia o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)