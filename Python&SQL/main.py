from config import DB_CONFIG
import mysql.connector

conexao = None

try:
    conexao = mysql.connector.connect(**DB_CONFIG)
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE  if not exists produtos(
     id int auto_increment PRIMARY KEY,
     nome varchar(255),
     preco decimal(10,2) not null,
     quantidade int,
     categoria varchar(50))""")

    conexao.commit()
    print("Tabela criada ")

except mysql.connector.Error as erro:
    print(erro)

finally:
    if conexao and conexao.is_connected():
        conexao.close()


