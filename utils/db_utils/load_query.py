def load_query(path_arq):
    try:
        with open(path_arq, 'r') as arq:
            return arq.read()
    except FileNotFoundError:
        print(f"Erro: arquivo {path_arq} nao foi encontrado")
    except PermissionError:
        print(f"Erro: permisao negada para acessar o arquivo {path_arq}")
    return None