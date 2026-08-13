import mysql


def criar_tabela():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id         INT           AUTO_INCREMENT PRIMARY KEY,
                nome       VARCHAR(100)  NOT NULL,
                preco      DECIMAL(10,2) NOT NULL,
                quantidade INT,
                categoria  VARCHAR(50)
            )
        """)

        conexao.commit()
        print("Tabela criada com sucesso!")

    except mysql.connector.Error as erro:
        print(f"Erro: {erro}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()

#criar_tabela()          #executar uma unica vez