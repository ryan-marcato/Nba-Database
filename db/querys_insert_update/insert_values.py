def insert_jogadores(id_jogador, nome_jogador, time_jogador):
    if time_jogador is None:
        query = f"""INSERT INTO tb_jogadores
                VALUES('{id_jogador}', "{nome_jogador}", NULL)"""
    
    query = f"""INSERT INTO tb_jogadores
                VALUES('{id_jogador}', "{nome_jogador}", "{time_jogador}")"""
    return query

def insert_times(id_time, nome_time, sigla_time):
    query = f"""INSERT INTO tb_times
                VALUES('{id_time}', "{nome_time}", "{sigla_time}")"""
    return query

def insert_estatisticas_jogadores(id_jogador, infos):
    posicao = infos[0]
    jogos_disputados = int(infos[1])
    min_por_jogo = float(infos[2])
    pontos_por_jogo = float(infos[3])
    avg_arremessos_convertidos = float(infos[4])
    avg_tentativa_arremessos = float(infos[5])
    porcentagem_arremessos_certos = float(infos[6])
    avg_arremessos_3pontos_convertidos = float(infos[7])
    avg_tentativas_arremessos_3pontos = float(infos[8])
    porcentagem_arremessos_3pontos_convertidos = float(infos[9])
    avg_lances_livres_convertidos = float(infos[10])
    avg_tentativa_lances_livres = float(infos[11])
    aproveitamento_lances_livres = float(infos[12])
    rebotes_por_jogo = float(infos[13])
    assistencia_por_jogo = float(infos[14])
    roubos_bola_por_jogo = float(infos[15])
    tocos_por_jogo = float(infos[16])
    erros_por_jogo = float(infos[17])
    duplo_duplo = int(infos[18])
    triplo_duplo = int(infos[19])
    
    query = f"""INSERT INTO tb_estatisticas_jogadores
                VALUES('{id_jogador}', '{posicao}', {jogos_disputados}, {min_por_jogo}, {pontos_por_jogo}, {avg_arremessos_convertidos},
                      {avg_tentativa_arremessos}, {porcentagem_arremessos_certos}, {avg_arremessos_3pontos_convertidos},
                      {avg_tentativas_arremessos_3pontos}, {porcentagem_arremessos_3pontos_convertidos}, {avg_lances_livres_convertidos},
                      {avg_tentativa_lances_livres}, {aproveitamento_lances_livres}, {rebotes_por_jogo},
                      {assistencia_por_jogo}, {roubos_bola_por_jogo}, {tocos_por_jogo},
                      {erros_por_jogo}, {duplo_duplo}, {triplo_duplo})"""    
    return query

def insert_estatisticas_times(id_time, infos):
    jogos_diputados = infos[0]
    pontos_por_jogo = infos[1]
    avg_arremessos_convertidos = infos[2]
    avg_tentativas_arremesos = infos[3]
    porcetagem_arremessos_certos = infos[4]
    avg_arremessos_3pontos_convertidos = infos[5]
    avg_tentativas_arremessos_3pontos =  infos[6]
    porcentagem_3pontos = infos[7]
    avg_lances_livres_convertidos =  infos[8]
    avg_tentativas_lances_livres = infos[9]
    aproveitamento_lance_livre = infos[10]
    rebotes_ofensivos_por_jogo = infos[11]
    rebotes_defensivos_por_jogo = infos[12]
    rebotes_por_jogo = infos[13]
    assistencia_por_jogo = infos[14]
    roubos_de_bola_por_jogo = infos[15]
    tocos_por_jogo = infos[16]
    erros_por_jogo = infos[17]
    faltas_por_jogo = infos[18]
    
    query  = f"""INSERT INTO tb_estatisticas_times
                 VALUES('{id_time}', {jogos_diputados}, {pontos_por_jogo},
                        {avg_arremessos_convertidos}, {avg_tentativas_arremesos}, {porcetagem_arremessos_certos},
                        {avg_arremessos_3pontos_convertidos}, {avg_tentativas_arremessos_3pontos}, {porcentagem_3pontos},
                        {avg_lances_livres_convertidos}, {avg_tentativas_lances_livres}, {aproveitamento_lance_livre},
                        {rebotes_ofensivos_por_jogo}, {rebotes_defensivos_por_jogo}, {rebotes_por_jogo},
                        {assistencia_por_jogo}, {roubos_de_bola_por_jogo}, {tocos_por_jogo},
                        {erros_por_jogo}, {faltas_por_jogo})"""
    return query