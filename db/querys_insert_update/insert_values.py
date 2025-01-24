def insert_jogadores(id_jogador, nome_jogador, time_jogador, posicao):
    query = f"""INSERT INTO tb_jogadores
                VALUES({id_jogador}, '{nome_jogador}', '{time_jogador}');"""
    return query

def insert_estatisticas(id_jogador, infos):
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
                      {erros_por_jogo}, {duplo_duplo}, {triplo_duplo});"""
    
    return query