CREATE TABLE IF NOT EXISTS tb_jogadores (
    id_jogador VARCHAR(100) PRIMARY KEY,
    nome_jogador VARCHAR(100) NOT NULL,
    time_jogador VARCHAR(3),
    posicao VARCHAR(2)
)