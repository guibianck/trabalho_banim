import sqlite3
conector = sqlite3.connect("automoveis.db")

cursor = conector.cursor()
try:
    sql = """
     create table clientes (
            CPF INTEGER PRIMARY KEY, 
           NOME STRING NOT NULL,
           RG INTEGER NOT NULL,
           ENDERECO STRING NOT NULL,
           EMAIL STRING UNIQUE NOT NULL,
           TEL_FIXO STRING NOT NULL,
           CELULAR STRING UNIQUE NOT NULL)
"""
    cursor.execute(sql)
    print("Tabela criada com sucesso")
except sqlite3.OperationalError:   
   pass  


def inserir_dados():
    cpf = int(input('Digite o cpf: '))
    nome = input('Digite o nome: ')
    rg = int(input('Digite o RG: '))
    endereco = input('Digite o endereco: ')
    email= input('Digite o email: ')
    tel_fixo = input('Digite o telefone fixo: ')
    celular = input('Digite o celular: ')
    inserir_dados_sql(cpf,nome,rg,endereco,email,tel_fixo,celular)
    print("Dados inseridos com sucesso")
    
    
def inserir_dados_sql(CPF,NOME,RG,ENDERECO,EMAIL,TEL_FIXO,CELULAR):
    sql = """
        insert into clientes(CPF,NOME,RG,ENDERECO,EMAIL,TEL_FIXO,CELULAR) values (?,?,?,?,?,?,?)
    """
    param =[CPF,NOME,RG,ENDERECO,EMAIL,TEL_FIXO,CELULAR]
    cursor.execute(sql,param)
    conector.commit() 
    cursor.close()
    conector.close()

inserir_dados()