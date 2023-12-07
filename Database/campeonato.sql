--Sera que da pra fazer a DDL em um arquivo, e as consultas em outros? SIM!!! Eh o mais certo!!!!
--E isso eh uma boa ideia?
-- Create TIME table
CREATE TABLE IF NOT EXISTS TIME (
    nome_principal TEXT NOT NULL,
    complemento TEXT NOT NULL,
    tecnico TEXT NOT NULL,
    estadio TEXT NOT NULL,
    cidade TEXT NOT NULL,
    vitorias INTEGER DEFAULT 0,
    empates INTEGER DEFAULT 0,
    derrotas INTEGER DEFAULT 0,
    PRIMARY KEY (nome_principal, complemento)
);

-- Create PARTIDA table
CREATE TABLE IF NOT EXISTS PARTIDA (
    num_partida INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    mandante_nome TEXT NOT NULL,
    mandante_complemento TEXT NOT NULL,
    visitante_nome TEXT NOT NULL,
    visitante_complemento TEXT NOT NULL,
    rodada INTEGER,
    data_hora INTEGER, -- Using unix timestamp. You need to use an SQLite function to convert
    arbitros TEXT,
    local TEXT,
    FOREIGN KEY (mandante_nome, mandante_complemento) REFERENCES TIME (nome_principal, complemento),
    FOREIGN KEY (visitante_nome, visitante_complemento) REFERENCES TIME (nome_principal, complemento )
);

-- Create JOGADOR table
CREATE TABLE IF NOT EXISTS JOGADOR (
    nome TEXT NOT NULL,
    apelido TEXT NOT NULL,
    posicao TEXT,
    time_atual_nome TEXT,
    time_atual_complemento TEXT,
    times_pass TEXT,
    data_nasc INTEGER,
    suspenso BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (nome, apelido),
    FOREIGN KEY (time_atual_nome) REFERENCES TIME (nome_principal),
    FOREIGN KEY (time_atual_complemento) REFERENCES TIME (complemento)
);

-- GOL table
CREATE TABLE IF NOT EXISTS GOL (
    tempo_partida INTEGER PRIMARY KEY NOT NULL,
    time_fez_nome TEXT NOT NULL,
    time_levou_nome TEXT NOT NULL, 
    jogador_fez TEXT, 
    jogador_assis TEXT, 
    tipo_gol TEXT,
    fora_de_casa BOOLEAN,
    partida INTEGER,
    FOREIGN KEY (partida) REFERENCES PARTIDA (num_partida)
);

-- FALTA table
CREATE TABLE IF NOT EXISTS FALTA (
    tempo_partida INTEGER PRIMARY KEY NOT NULL,
    time_faltoso TEXT, 
    participante_faltoso TEXT,
    tipo_falta TEXT,
    cartao TEXT,
    partida INTEGER,
    FOREIGN KEY (partida) REFERENCES PARTIDA (num_partida)
);

-- JOGA table
CREATE TABLE IF NOT EXISTS JOGA (
    nome_jogador TEXT,
    apelido_jogador TEXT,
    posicao_jogador TEXT,
    num_partida INTEGER,
    substituicoes_id INTEGER,
    FOREIGN KEY (nome_jogador) REFERENCES JOGADOR (nome),
    FOREIGN KEY (apelido_jogador) REFERENCES JOGADOR (apelido),
    FOREIGN KEY (num_partida) REFERENCES PARTIDA (num_partida),
    FOREIGN KEY (substituicoes_id) REFERENCES SUBSTITUICOES (substituicoes_id)
);

-- TIMES_PASS table
CREATE TABLE IF NOT EXISTS TIMES_PASS (
    nome_jogador TEXT,
    apelido_jogador TEXT,
    nome_time TEXT,
    FOREIGN KEY (nome_jogador) REFERENCES JOGADOR (nome),
    FOREIGN KEY (apelido_jogador) REFERENCES JOGADOR (apelido)
);

-- Create SUBSTITUICOES table
CREATE TABLE IF NOT EXISTS SUBSTITUICOES (
    substituicoes_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome_jogador_entra TEXT,
    apelido_jogador_entra TEXT,
    nome_jogador_sai TEXT,
    apelido_jogador_sai TEXT,
    tempo_partida INTEGER,
    num_partida INTEGER,
    FOREIGN KEY (num_partida) REFERENCES PARTIDA (num_partida)
);
