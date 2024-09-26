import sqlite3

conector = sqlite3.connect("automoveis.db")
conector.execute("PRAGMA foreign_keys = ON") 
cursor = conector.cursor()

try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            COD_PROD INTEGER PRIMARY KEY AUTOINCREMENT,
            DESCRICAO TEXT NOT NULL,
            PRECO REAL NOT NULL,
            QUANTIDADE INTEGER NOT NULL,
            COD_FORN INTEGER NOT NULL,
            FOREIGN KEY(COD_FORN) REFERENCES fornecedores(COD_FORN) ON DELETE CASCADE)
    """)
    print("Tabela produtos criada com sucesso")
except sqlite3.OperationalError:
    pass  

def inserir_dados():
    descricao = input('Digite a descrição do produto: ')
    preco = float(input('Digite o preço do produto: R$'))
    quantidade = int(input('Digite a quantidade do produto: '))
    cod_forn = int(input('Digite o código do fornecedor: '))
    try:
        inserir_dados_sql(descricao, preco, quantidade, cod_forn)
        print("Dados inseridos com sucesso")
    except sqlite3.IntegrityError:
        print("Erro: O código do fornecedor não existe.")

def inserir_dados_sql(DESCRICAO, PRECO, QUANTIDADE, COD_FORN):
    sql = """
        INSERT INTO produtos (DESCRICAO, PRECO, QUANTIDADE, COD_FORN) VALUES (?, ?, ?, ?)
    """
    param = [DESCRICAO, PRECO, QUANTIDADE, COD_FORN]
    cursor.execute(sql, param)
    conector.commit() 


def fechar_conexao():
    cursor.close()
    conector.close()


inserir_dados()
fechar_conexao()
