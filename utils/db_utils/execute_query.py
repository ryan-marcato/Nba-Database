from utils.db_utils.conection_db import create_conection
from sqlalchemy import text, exc

def query_execute_tb(query):
    try:
        conexao = create_conection()
        if conexao is None:
            print("Nao foi possivel abrir conexao")
            return
    
        with conexao:
            conexao.execute(text(query))
            print("Query executadada com sucesso")
    except exc.SQLAlchemyError as e:
        print(f"Nao foi possivel executar a query: {e}")

#Funçao para insert e update
#commit para confirmar a transação
def query_insert_execute(query):
    try:
        conexao = create_conection()
        if conexao is None:
            print("Nao foi possivel abrir conexao")
            return
        
        with conexao:
            conexao.execute(text(query))
            conexao.commit() 
            print("Query executada com sucesso")
    except exc.SQLAlchemyError as e:
        print(f"Nao foi possivel executar a query: {e}")