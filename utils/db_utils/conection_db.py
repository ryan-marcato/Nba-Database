from utils.db_utils.info_conection import info_conetion
from sqlalchemy import create_engine, exc

DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME  = info_conetion()

def create_conection():
    try:
        engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        return engine.connect()
    except exc.SQLAlchemyError as e:
        print(f"Erro ao tentar conexao com o banco de dados: {e}")
        return None