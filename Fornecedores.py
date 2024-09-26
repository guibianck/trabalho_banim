import sqlite3
conector = sqlite3.connect("automoveis.db")

cursor = conector.cursor()
try:
    sql = """
     create table fornecedores (
            COD_FORN INTEGER PRIMARY KEY AUTOINCREMENT,
           RAZ_SOCIAL STRING UNIQUE NOT NULL,
           NOME_FANT STRING UNIQUE NOT NULL,
           CNPJ STRING UNIQUE NOT NULL,
           ENDERECO STRING NOT NULL,
           TELEFONE STRING NOT NULL)
           
"""
#NOME_CTT STRING FOREIGN KEY)
    cursor.execute(sql)
    print("Tabela criada com sucesso")
except sqlite3.OperationalError:   
   pass  


def inserir_dados():
    raz_social = input('Digite a razão social: ')
    nome_fant = input('Digite o nome fantasia: ')
    cnpj = input('Digite o CNPJ: ')
    endereco = input('Digite o endereco: ')
    telefone = input('Digite o telefone: ')
    inserir_dados_sql(raz_social,nome_fant,cnpj,endereco,telefone)
    print("Dados inseridos com sucesso")
    
    
def inserir_dados_sql(RAZ_SOCIAL,NOME_FANT,CNPJ,ENDERECO,TELEFONE):
    sql = """
        insert into fornecedores (RAZ_SOCIAL,NOME_FANT,CNPJ,ENDERECO,TELEFONE) values (?,?,?,?,?)
    """
    param =[RAZ_SOCIAL,NOME_FANT,CNPJ,ENDERECO,TELEFONE]
    cursor.execute(sql,param)
    conector.commit() 
    cursor.close()
    conector.close()

inserir_dados()