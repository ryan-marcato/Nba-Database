from utils.db_utils.load_query import load_query
from utils.db_utils.execute_query import query_execute_tb

query01 = load_query('db/create_tb/jogadores.sql')
query02 = load_query('db/create_tb/estatisticas_jogadores.sql')

if query01 is None or query02 is None:
    print("Erro ao ler as querys")
    
query_execute_tb(query01)
query_execute_tb(query02)