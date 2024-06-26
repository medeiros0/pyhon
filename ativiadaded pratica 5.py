import mysql.connector


def create_connection():
    con = mysql.connector.connect(user='root',
                                   password='ceub123456',
                                   host='127.0.0.1',
                                   database='db_hogwarts')
    print('Conexão:', con)
    return con


def close_connection(cursor, conexao):
    cursor.close()
    conexao.close()
    print('\nConexão fechada.')


def create_table_hogwarts(cursor):
    sql = """CREATE TABLE if not exists tb_hogwarts(
        id INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(45) NOT NULL UNIQUE,
        casa ENUM('Grifinória', 'Sonserina', 'Corvinal', 'Lufa-Lufa') NOT NULL,
        dta_nascimento DATE,
        PRIMARY KEY (id)
    )"""
    cursor.execute(sql)


def create_table_domain(cursor):
    sql = """CREATE TABLE if not exists tb_domain(
        id INT NOT NULL AUTO_INCREMENT,
        column1 VARCHAR(45) NOT NULL UNIQUE,
        PRIMARY KEY (id)
    )"""
    cursor.execute(sql)


def insert_hogwarts(cursor, conexao):
    a_nome = input('Insert - Nome: ')
    a_casa = input('Casa (Grifinória/Sonserina/Corvinal/Lufa-Lufa): ')
    a_data = input("Data de nascimento (aaaa-mm-dd): ")
    sql = f"""INSERT INTO tb_hogwarts (nome, casa, dta_nascimento) 
              VALUES ('{a_nome}', '{a_casa}', '{a_data}')"""
    cursor.execute(sql)
    conexao.commit()


def insert_domain(cursor, conexao):
    data = input('Insert - Column1: ')
    sql = f"INSERT INTO tb_domain (column1) VALUES ('{data}')"
    cursor.execute(sql)
    conexao.commit()


def select_hogwarts(cursor):
    print('- Consulta:')
    sql = 'SELECT * FROM tb_hogwarts'
    cursor.execute(sql)
    l_registros = cursor.fetchall()
    print('- List of tuples:')
    print(l_registros)
    print('- Tuples:')
    for record in l_registros:
        print(record)


def select_domain(cursor):
    print('- Consulta:')
    sql = 'SELECT * FROM tb_domain'
    cursor.execute(sql)
    l_registros = cursor.fetchall()
    print('- List of tuples:')
    print(l_registros)
    print('- Tuples:')
    for record in l_registros:
        print(record)


def main():
    conexao = create_connection()
    cursor = conexao.cursor()

    create_table_hogwarts(cursor)
    create_table_domain(cursor)

    while True:
        print("\nMENU:")
        print("1. Inserir dados na tabela Hogwarts")
        print("2. Inserir dados na tabela Domain")
        print("3. Selecionar todos os registros da tabela Hogwarts")
        print("4. Selecionar todos os registros da tabela Domain")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            insert_hogwarts(cursor, conexao)
        elif choice == "2":
            insert_domain(cursor, conexao)
        elif choice == "3":
            select_hogwarts(cursor)
        elif choice == "4":
            select_domain(cursor)
        elif choice == "5":
            close_connection(cursor, conexao)
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
