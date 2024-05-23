# import mysql.connector 


# conexao = mysql.connector.connect(
#      host="127.0.0.1",
#      user="root",
#      password="admin",
# )


# cursor = conexao.cursor()

# comando_sql = "CREATE DATABASE bd_aula"


# cursor.execute(comando_sql)


# cursor.close()
# conexao.close()

#Programa inicial bruto 


# import mysql.connector


# conexao = mysql.connector.connect(
#      host="127.0.0.1",
#      user="root",
#      password="admin",
#      database="bd_aula"
# )

# cursor = conexao.cursor()


# comando_sql = """
# CREATE TABLE minha_tabela (
#     id INT PRIMARY KEY,
#     nome VARCHAR(100) NOT NULL,
#     sobrenome VARCHAR(100) NOT NULL,
#     idade INT,
#     salario DECIMAL(10, 2),
#     endereco VARCHAR(50)
# )
# """


# cursor.execute(comando_sql)
# cursor.close()
# conexao.close()

#criando a tabela 


import mysql.connector


conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="admin",
    database="bd_aula"
)


cursor = conexao.cursor()


comando_sql = """
INSERT INTO minha_tabela (nome, sobrenome, idade, salario, endereco)
VALUES (%s, %s, %s, %s, %s)
"""

dados = [
    ("Fernando", "Farias", 30, 3000.50, "Rua A, 123"),
    ("Eduardo", "Frois", 25, 2500.75, "Avenida B, 321")
]

cursor.executemany(comando_sql, dados)

conexao.commit()

cursor.close()
conexao.close()

print("Dados inseridos com sucesso!")

#programa para inserir dados