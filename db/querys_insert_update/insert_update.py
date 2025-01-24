def update_jogadores(id_jogador, nome_jogador, time_jogador, posicao):
    query = f"""UPDATE tb_jogadores
                SET nome_jogador={nome_jogador}, time_jogador={time_jogador}, posicao={posicao}
                WHERE id_jogador={id_jogador};"""
                
def update_estatisticas(id_jogador, infos):
    jogos_disputados = infos[0]
    min_por_jogo = infos[1]
    pontos_por_jogo = infos[2]
    avg_arremessos_convertidos = infos[3]
    avg_tentativa_arremessos = infos[4]
    porcentagem_arremessos_certos = infos[5]
    avg_arremessos_3pontos_convertidos = infos[6]
    avg_tentativas_arremessos_3pontos = infos[7]
    porcentagem_arremessos_3pontos_convertidos = infos[8]
    avg_lances_livres_convertidos = infos[9]
    avg_tentativa_lances_livres = infos[10]
    aproveitamento_lances_livres = infos[11]
    rebotes_por_jogo = infos[12]
    assistencia_por_jogo = infos[13]
    roubos_bola_por_jogo = infos[14]
    tocos_por_jogo = infos[15]
    erros_por_jogo = infos[16]
    duplo_duplo = infos[17]
    triplo_duplo = infos[18]
    
    query = f"""UPDATE tb_estatisticas_jogadores
                SET 
                   jogos_disputados={jogos_disputados}, min_por_jogo={min_por_jogo}, pontos_por_jogo={pontos_por_jogo},
                   avg_arremessos_convertidos={avg_arremessos_convertidos},  avg_tentativa_arremessos={avg_tentativa_arremessos}, porcentagem_arremessos_certos={porcentagem_arremessos_certos},
                   avg_arremessos_3pontos_convertidos={avg_arremessos_3pontos_convertidos}, avg_tentativas_arremessos_3pontos={avg_tentativas_arremessos_3pontos },
                   porcentagem_arremessos_3pontos_convertidos={porcentagem_arremessos_3pontos_convertidos}, avg_lances_livres_convertidos={avg_lances_livres_convertidos},
                   avg_tentativa_lances_livres={avg_tentativa_lances_livres}, aproveitamento_lances_livres={aproveitamento_lances_livres}, rebotes_por_jogo={rebotes_por_jogo},
                   assistencia_por_jogo={assistencia_por_jogo}, roubos_bola_por_jogo={roubos_bola_por_jogo}, tocos_por_jogo={tocos_por_jogo},
                   erros_por_jogo={erros_por_jogo}, duplo_duplo={duplo_duplo}, triplo_duplo={triplo_duplo}
                WHERE id_jogador={id_jogador}"""