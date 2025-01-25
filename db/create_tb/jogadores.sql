CREATE TABLE IF NOT EXISTS tb_jogadores (
    id_jogador VARCHAR(100) PRIMARY KEY,
    nome_jogador VARCHAR(100) NOT NULL,
    time_jogador VARCHAR(10),
    CONSTRAINT fk_sigla_time FOREIGN KEY (time_jogador) REFERENCES tb_times (sigla_time)
)