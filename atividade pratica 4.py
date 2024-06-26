import mysql.connector
def create_database():
    conexao_db = mysql.connector.connect(user='root',  
                            password='ceub123456',              
                            host='127.0.0.1')          
                            
    print('Conexão db:', conexao_db)  
    cursor_db = conexao_db.cursor()   
    sql = "CREATE DATABASE if not exists db_hogwarts"
    cursor_db.execute(sql)           
    cursor_db.close()
    conexao_db.close()
    print('\nConexão db fechada.')
    

def create_connection():
    con = mysql.connector.connect(user='root',      
                            password='',            
                            host='127.0.0.1',       
                            database='db_hogwarts')   
    print('Conexão:', con)                          
    return con


def close_connection():  
    cursor.close()
    conexao.close()
    print('\nConexão fechada.')


def create_table():
    sql = """ CREATE TABLE if not exists tb_hogwarts(
    idt INT NOT NULL AUTO_INCREMENT,    
    nome VARCHAR(45) NOT NULL UNIQUE,  
    casa VARCHAR(45) NOT NULL,
    dta_nascimento DATE NULL,                   
    PRIMARY KEY (idt)                  
    )   """
    cursor.execute(sql)


def insert():                               
    a_nome = input('Insert - Nome: ')
    a_casa = input('Casa: ')
    a_data = input("Data aaaa-mm-dd")
    sql = f""" insert into tb_hogwarts (nome, casa, dta_nascimento) 
                      values ('{a_nome}', {a_casa},{a_data})  """
    cursor.execute(sql)
    conexao.commit()                    
    

def select():    
    print('- Consulta:')
    sql = ' select * from tb_hogwarts '
    cursor.execute(sql)
    l_registros = cursor.fetchall()     
    print('- List of tuplas:')          
    print(l_registros)                  
    print(' - Tuplas:')                 
    for record in l_registros:  
        print(record)
        
    print("- Colunas, notação de vetor:")       
    for record in l_registros:
        print("- Idt:", record[0])
        print("Nome:", record[1])
        print("Casa:", record[2])
        print("Data de nascimento", record[3])
        

def delete():
    x = int(input("informe qual aluno vc deseja excluir"))
    sql = f"delete from tb_hogwarts WHERE idt = {x}"
    cursor.execute(sql)
    conexao.commit() 

if __name__ == '__main__':
    create_database()                   
    conexao = create_connection()       
    cursor = conexao.cursor()
    create_table()

    valor = int(input("Digite qual ação você deseja realizar\n[1]insert\n[2]delete\n[3]read"))
    while (valor !=4):
        if valor > 3:
            print("informe um valor valido")
            break
        if valor == 1:
            insert()
            break
        if valor == 2:
            delete()
            break
        if valor == 3:
            select()
            break                                                  

    close_connection()