import sqlite3
conector = sqlite3.connect("automoveis.db")

cursor = conector.cursor()

sql = """
     create table produtos (
            COD_PROD INTEGER PRIMARY KEY AUTOINCREMENT,
           DESCRICAO STRING NOT NULL,
           PRECO NUMERIC NOT NULL,
           QUANTIDADE INTEGER NOT NULL,
           COD_FORN INTEGER NOT NULL,
           FOREIGN KEY(COD_FORN) REFERENCES fornecedores(COD_FORN)ON DELETE CASCADE )
"""
cursor.execute(sql)
print("Tabela criada com sucesso")
  


def inserir_dados():
    descricao = input('Digite a descrição do produto: ')
    preco = int(input('Digite o preço do produto: R$'))
    quantidade = input('Digite a quantidade do produto: ')
    inserir_dados_sql(descricao,preco,quantidade)
    print("Dados inseridos com sucesso")
    
    
def inserir_dados_sql(DESCRICAO,PRECO,QUANTIDADE):
    sql = """
        insert into produtos (DESCRICAO,PRECO,QUANTIDADE) values (?,?,?)
    """
    param =[DESCRICAO,PRECO,QUANTIDADE]
    cursor.execute(sql,param)
    conector.commit() 
    cursor.close()
    conector.close()

inserir_dados()