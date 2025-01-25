CREATE TABLE IF NOT EXISTS tb_times(
    id_time VARCHAR(100) PRIMARY KEY,
    nome_time VARCHAR(60),
    sigla_time VARCHAR(10) UNIQUE
)