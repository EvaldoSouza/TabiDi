
-- Inserir times do Campeonato Brasileiro na tabela TIME
INSERT INTO TIME (nome_principal, complemento, tecnico, estadio, cidade, vitorias, empates, derrotas)
VALUES ('Flamengo', 'RJ', 'Renato Gaúcho', 'Maracanã', 'Rio de Janeiro', 0, 0, 0);

INSERT INTO TIME (nome_principal, complemento, tecnico, estadio, cidade, vitorias, empates, derrotas)
VALUES ('Palmeiras', 'SP', 'Abel Ferreira', 'Allianz Parque', 'São Paulo', 0, 0, 0);

INSERT INTO TIME (nome_principal, complemento, tecnico, estadio, cidade, vitorias, empates, derrotas)
VALUES ('São Paulo', 'SP', 'Hernán Crespo', 'Morumbi', 'São Paulo', 0, 0, 0);

INSERT INTO TIME (nome_principal, complemento, tecnico, estadio, cidade, vitorias, empates, derrotas)
VALUES ('Atlético Mineiro', 'MG', 'Cuca', 'Mineirão', 'Belo Horizonte', 0, 0, 0);

INSERT INTO TIME (nome_principal, complemento, tecnico, estadio, cidade, vitorias, empates, derrotas)
VALUES ('Fluminense', 'RJ', 'Marcos Felipe', 'Maracanã', 'Rio de Janeiro', 0, 0, 0);

-- Inserir jogadores no time "Flamengo"
-- Primeiros 10 jogadores
INSERT INTO JOGADOR (nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc, suspenso)
VALUES
    ('Gabriel Barbosa', 'Gabigol', 'Atacante', 'Flamengo', 'RJ', NULL, '1996-08-30', 0),
    ('Bruno Henrique', 'Bruno', 'Atacante', 'Flamengo', 'RJ', NULL, '1990-12-30', 0),
    ('Éverton Ribeiro', 'Everton', 'Meia', 'Flamengo', 'RJ', NULL, '1989-04-10', 0),
    ('Arrascaeta', 'Arrascaeta', 'Meia', 'Flamengo', 'RJ', NULL, '1994-03-01', 0),
    ('Diego Alves', 'Diego', 'Goleiro', 'Flamengo', 'RJ', NULL, '1985-06-24', 0),
    ('Willian Arão', 'Arão', 'Meio-Campista', 'Flamengo', 'RJ', NULL, '1992-03-17', 0),
    ('Rodrigo Caio', 'Caio', 'Zagueiro', 'Flamengo', 'RJ', NULL, '1993-08-17', 0),
    ('Gerson', 'Gerson', 'Meia', 'Flamengo', 'RJ', NULL, '1997-05-20', 0),
    ('Thiago Maia', 'Thiago', 'Meio-Campista', 'Flamengo', 'RJ', NULL, '1997-03-23', 0),
    ('Michael', 'Michael', 'Atacante', 'Flamengo', 'RJ', NULL, '1996-12-22', 0);

-- Segundos 10 jogadores
INSERT INTO JOGADOR (nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc, suspenso)
VALUES
    ('Pedro', 'Pedro', 'Atacante', 'Flamengo', 'RJ', NULL, '1997-09-20', 0),
    ('Renê', 'Renê', 'Lateral', 'Flamengo', 'RJ', NULL, '1992-09-20', 0),
    ('Léo Pereira', 'Léo', 'Zagueiro', 'Flamengo', 'RJ', NULL, '1996-02-11', 0),
    ('Vitinho', 'Vitinho', 'Atacante', 'Flamengo', 'RJ', NULL, '1993-10-09', 0),
    ('Hugo Souza', 'Hugo', 'Goleiro', 'Flamengo', 'RJ', NULL, '1999-02-04', 0),
    ('Gustavo Henrique', 'Gustavo', 'Zagueiro', 'Flamengo', 'RJ', NULL, '1993-07-29', 0),
    ('Matheuzinho', 'Matheuzinho', 'Lateral', 'Flamengo', 'RJ', NULL, '1999-08-20', 0),
    ('Piris da Motta', 'Piris', 'Meio-Campista', 'Flamengo', 'RJ', NULL, '1994-03-01', 0),
    ('Mateus Vital', 'Mateus', 'Meia', 'Flamengo', 'RJ', NULL, '1998-02-05', 0),
    ('Pedro Rocha', 'Pedro', 'Atacante', 'Flamengo', 'RJ', NULL, '1995-12-01', 0);

-- Inserir mais jogadores do Flamengo conforme necessário
-- Inserir jogadores no time "Palmeiras"
-- Primeiros 10 jogadores
INSERT INTO JOGADOR (nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc, suspenso)
VALUES
    ('Luiz Adriano', 'Luiz', 'Atacante', 'Palmeiras', 'SP', NULL, '1987-04-12', 0),
    ('Gustavo Scarpa', 'Scarpa', 'Meia', 'Palmeiras', 'SP', NULL, '1994-01-05', 0),
    ('Rony', 'Rony', 'Atacante', 'Palmeiras', 'SP', NULL, '1995-05-11', 0),
    ('Weverton', 'Weverton', 'Goleiro', 'Palmeiras', 'SP', NULL, '1987-12-13', 0),
    ('Danilo', 'Danilo', 'Meio-Campista', 'Palmeiras', 'SP', NULL, '1999-06-10', 0),
    ('Felipe Melo', 'Felipe', 'Meio-Campista', 'Palmeiras', 'SP', NULL, '1983-08-26', 0),
    ('Marcos Rocha', 'Marcos', 'Lateral', 'Palmeiras', 'SP', NULL, '1988-12-11', 0),
    ('Zé Rafael', 'Zé', 'Meia', 'Palmeiras', 'SP', NULL, '1993-01-16', 0),
    ('Luan', 'Luan', 'Zagueiro', 'Palmeiras', 'SP', NULL, '1993-03-11', 0),
    ('Matías Viña', 'Matías', 'Lateral', 'Palmeiras', 'SP', NULL, '1997-06-09', 0);

-- Segundos 10 jogadores
INSERT INTO JOGADOR (nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc, suspenso)
VALUES
    ('Raphael Veiga', 'Raphael', 'Meia', 'Palmeiras', 'SP', NULL, '1995-05-02', 0),
    ('Deyverson', 'Deyverson', 'Atacante', 'Palmeiras', 'SP', NULL, '1991-05-23', 0),
    ('Gustavo Gomez', 'Gustavo', 'Zagueiro', 'Palmeiras', 'SP', NULL, '1993-05-06', 0),
    ('Mayke', 'Mayke', 'Lateral', 'Palmeiras', 'SP', NULL, '1992-02-09', 0),
    ('Renan', 'Renan', 'Goleiro', 'Palmeiras', 'SP', NULL, '2000-05-24', 0),
    ('Renan', 'Renanzinho', 'Zagueiro', 'Palmeiras', 'SP', NULL, '2000-02-21', 0),
    ('Gabriel Menino', 'Gabriel', 'Meio-Campista', 'Palmeiras', 'SP', NULL, '2000-09-29', 0),
    ('Giovani', 'Giovani', 'Atacante', 'Palmeiras', 'SP', NULL, '2001-08-10', 0),
    ('Gabriel Silva', 'Gabriel', 'Atacante', 'Palmeiras', 'SP', NULL, '2001-09-18', 0),
    ('Patrick de Paula', 'Patrick', 'Meio-Campista', 'Palmeiras', 'SP', NULL, '1999-11-24', 0);

-- Inserir mais jogadores do Palmeiras conforme necessário
-- Inserir jogadores no time "São Paulo"
-- Primeiros 10 jogadores
INSERT INTO JOGADOR (nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc, suspenso)
VALUES
    ('Luciano', 'Luciano', 'Atacante', 'São Paulo', 'SP', NULL, '1993-03-19', 0),
    ('Eder', 'Eder', 'Atacante', 'São Paulo', 'SP', NULL, '1986-11-17', 0),
    ('Daniel Alves', 'Daniel', 'Meio-Campista', 'São Paulo', 'SP', NULL, '1983-05-06', 0),
    ('Miranda', 'Miranda', 'Zagueiro', 'São Paulo', 'SP', NULL, '1984-09-07', 0),
    ('Luan', 'Luanzinho', 'Meia', 'São Paulo', 'SP', NULL, '1993-04-18', 0),
    ('Arboleda', 'Arboleda', 'Zagueiro', 'São Paulo', 'SP', NULL, '1991-10-22', 0),
    ('Marquinhos', 'Marquinhos', 'Meio-Campista', 'São Paulo', 'SP', NULL, '1997-09-25', 0),
    ('Rigoni', 'Rigoni', 'Meia', 'São Paulo', 'SP', NULL, '1993-08-09', 0),
    ('Bruno Alves', 'Bruno', 'Zagueiro', 'São Paulo', 'SP', NULL, '1991-03-16', 0),
    ('Vitor Bueno', 'Vitor', 'Meio-Campista', 'São Paulo', 'SP', NULL, '1994-01-07', 0);

-- Segundos 10 jogadores
INSERT INTO JOGADOR (nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc, suspenso)
VALUES
    ('Tiago Volpi', 'Tiago', 'Goleiro', 'São Paulo', 'SP', NULL, '1990-11-19', 0),
    ('Reinaldo', 'Reinaldo', 'Lateral', 'São Paulo', 'SP', NULL, '1989-03-21', 0),
    ('Galeano', 'Galeano', 'Lateral', 'São Paulo', 'SP', NULL, '1998-07-10', 0),
    ('Nestor', 'Nestor', 'Meio-Campista', 'São Paulo', 'SP', NULL, '2000-02-14', 0),
    ('Walce', 'Walce', 'Zagueiro', 'São Paulo', 'SP', NULL, '1999-05-04', 0),
    ('Lucas Perri', 'Lucas', 'Goleiro', 'São Paulo', 'SP', NULL, '1997-03-16', 0),
    ('Tchê Tchê', 'Tchê', 'Meio-Campista', 'São Paulo', 'SP', NULL, '1992-03-22', 0),
    ('Hernanes', 'Hernanes', 'Meio-Campista', 'São Paulo', 'SP', NULL, '1985-05-29', 0),
    ('Jonas Toró', 'Toró', 'Atacante', 'São Paulo', 'SP', NULL, '1999-12-19', 0),
    ('Brenner', 'Brenner', 'Atacante', 'São Paulo', 'SP', NULL, '2000-01-16', 0);

-- Inserir mais jogadores do São Paulo conforme necessário
-- Inserir jogadores no time "Fluminense"
-- Primeiros 10 jogadores
INSERT INTO JOGADOR (nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc, suspenso)
VALUES
    ('Fred', 'Fred', 'Atacante', 'Fluminense', 'RJ', NULL, '1983-10-03', 0),
    ('Nenê', 'Nenê', 'Meio-Campista', 'Fluminense', 'RJ', NULL, '1981-07-19', 0),
    ('Martinelli', 'Martinelli', 'Meio-Campista', 'Fluminense', 'RJ', NULL, '2001-06-22', 0),
    ('Yago Felipe', 'Yago', 'Meio-Campista', 'Fluminense', 'RJ', NULL, '1995-12-23', 0),
    ('Lucca', 'Lucca', 'Atacante', 'Fluminense', 'RJ', NULL, '1990-04-14', 0),
    ('John Kennedy', 'John', 'Atacante', 'Fluminense', 'RJ', NULL, '2002-05-17', 0),
    ('Cazares', 'Cazares', 'Meio-Campista', 'Fluminense', 'RJ', NULL, '1992-11-09', 0),
    ('Egídio', 'Egídio', 'Lateral', 'Fluminense', 'RJ', NULL, '1986-11-16', 0),
    ('Luccas Claro', 'Luccas', 'Zagueiro', 'Fluminense', 'RJ', NULL, '1992-08-23', 0),
    ('Caio Paulista', 'Caio', 'Atacante', 'Fluminense', 'RJ', NULL, '1998-02-11', 0);

-- Segundos 10 jogadores
INSERT INTO JOGADOR (nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc, suspenso)
VALUES
    ('Samuel Xavier', 'Samuel', 'Lateral', 'Fluminense', 'RJ', NULL, '1990-03-06', 0),
    ('Wellington', 'Wellington', 'Meio-Campista', 'Fluminense', 'RJ', NULL, '1991-02-16', 0),
    ('Hudson', 'Hudson', 'Meio-Campista', 'Fluminense', 'RJ', NULL, '1988-03-08', 0),
    ('Fernando Pacheco', 'Fernando', 'Atacante', 'Fluminense', 'RJ', NULL, '1999-04-11', 0),
    ('Lucca', 'Luccazinho', 'Atacante', 'Fluminense', 'RJ', NULL, '1994-02-08', 0),
    ('Yuri Lima', 'Yuri', 'Meio-Campista', 'Fluminense', 'RJ', NULL, '1994-01-15', 0),
    ('Higor', 'Higor', 'Meio-Campista', 'Fluminense', 'RJ', NULL, '1998-09-30', 0),
    ('Manoel', 'Manoel', 'Zagueiro', 'Fluminense', 'RJ', NULL, '1999-03-27', 0),
    ('Davi', 'Davi', 'Zagueiro', 'Fluminense', 'RJ', NULL, '2002-08-12', 0),
    ('Felipe', 'Felipe', 'Goleiro', 'Fluminense', 'RJ', NULL, '2001-05-20', 0);

-- Inserir mais jogadores do Fluminense conforme necessário
-- Inserir jogadores no time "Atlético Mineiro"
-- Primeiros 10 jogadores
INSERT INTO JOGADOR (nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc, suspenso)
VALUES
    ('Savarino', 'Savarino', 'Atacante', 'Atlético Mineiro', 'MG', NULL, '1996-05-11', 0),
    ('Eduardo Vargas', 'Vargas', 'Atacante', 'Atlético Mineiro', 'MG', NULL, '1989-11-20', 0),
    ('Nacho Fernández', 'Nacho', 'Meio-Campista', 'Atlético Mineiro', 'MG', NULL, '1990-01-04', 0),
    ('Keno', 'Keno', 'Atacante', 'Atlético Mineiro', 'MG', NULL, '1989-09-10', 0),
    ('Hyoran', 'Hyoran', 'Meio-Campista', 'Atlético Mineiro', 'MG', NULL, '1993-06-16', 0),
    ('Nathan', 'Nathan', 'Meio-Campista', 'Atlético Mineiro', 'MG', NULL, '1995-03-13', 0),
    ('Junior Alonso', 'Junior', 'Zagueiro', 'Atlético Mineiro', 'MG', NULL, '1993-02-09', 0),
    ('Sasha', 'Sasha', 'Atacante', 'Atlético Mineiro', 'MG', NULL, '1992-07-27', 0),
    ('Mariano', 'Mariano', 'Lateral', 'Atlético Mineiro', 'MG', NULL, '1986-04-23', 0),
    ('Réver', 'Réver', 'Zagueiro', 'Atlético Mineiro', 'MG', NULL, '1984-01-01', 0);

-- Segundos 10 jogadores
INSERT INTO JOGADOR (nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc, suspenso)
VALUES
    ('Zaracho', 'Zaracho', 'Meio-Campista', 'Atlético Mineiro', 'MG', NULL, '1999-03-16', 0),
    ('Eduardo Sasha', 'Sasha', 'Atacante', 'Atlético Mineiro', 'MG', NULL, '1992-07-18', 0),
    ('Réver', 'Réverinho', 'Zagueiro', 'Atlético Mineiro', 'MG', NULL, '1984-01-04', 0),
    ('Marlon', 'Marlon', 'Lateral', 'Atlético Mineiro', 'MG', NULL, '1999-08-29', 0),
    ('Igor Rabello', 'Igor', 'Zagueiro', 'Atlético Mineiro', 'MG', NULL, '1995-02-26', 0),
    ('Gabriel', 'Gabriel', 'Goleiro', 'Atlético Mineiro', 'MG', NULL, '1997-07-22', 0),
    ('Marrony', 'Marrony', 'Atacante', 'Atlético Mineiro', 'MG', NULL, '1999-01-18', 0),
    ('Borrero', 'Borrero', 'Meio-Campista', 'Atlético Mineiro', 'MG', NULL, '1998-01-26', 0),
    ('Guga', 'Guga', 'Lateral', 'Atlético Mineiro', 'MG', NULL, '1999-12-10', 0),
    ('Matheus Mendes', 'Matheus', 'Goleiro', 'Atlético Mineiro', 'MG', NULL, '2001-05-13', 0);

-- Inserir mais jogadores do Atlético Mineiro conforme necessário
-- Inserções fictícias na tabela FALTA
INSERT INTO FALTA (tempo_partida, time_faltoso, participante_faltoso, tipo_falta, cartao, partida)
VALUES
    (30, 'Flamengo', 'Gabriel', 'Falta dura', 'Cartão Amarelo', 1),
    (45, 'Flamengo', 'Diego', 'Mão na bola', 'Sem Cartão', 1),
    (55, 'Palmeiras', 'Felipe Melo', 'Entrada forte', 'Cartão Amarelo', 1),
    (72, 'São Paulo', 'Reinaldo', 'Simulação', 'Cartão Amarelo', 2),
    (88, 'Fluminense', 'Nenê', 'Falta tática', 'Cartão Amarelo', 2),
    (40, 'Atlético Mineiro', 'Guga', 'Falta de marcação', 'Cartão Amarelo', 3),
    (70, 'Palmeiras', 'Raphael Veiga', 'Falta técnica', 'Cartão Amarelo', 3),
    (75, 'São Paulo', 'Daniel Alves', 'Falta tática', 'Cartão Amarelo', 4),
    (28, 'Fluminense', 'Fred', 'Falta de marcação', 'Cartão Amarelo', 4),
    (60, 'Flamengo', 'Everton Ribeiro', 'Entrada forte', 'Cartão Amarelo', 5),
    (82, 'Atlético Mineiro', 'Vargas', 'Falta dura', 'Cartão Amarelo', 5),
    (42, 'São Paulo', 'Luciano', 'Simulação', 'Cartão Amarelo', 6),
    (53, 'Fluminense', 'Nenê', 'Falta tática', 'Cartão Amarelo', 6),
    (48, 'Palmeiras', 'Gustavo Gómez', 'Falta tática', 'Cartão Amarelo', 7),
    (60, 'Atlético Mineiro', 'Allan', 'Falta de marcação', 'Cartão Amarelo', 7),
    (25, 'Flamengo', 'Bruno Henrique', 'Falta técnica', 'Cartão Amarelo', 8),
    (35, 'São Paulo', 'Reinaldo', 'Falta tática', 'Cartão Amarelo', 8),
    (70, 'Fluminense', 'Nenê', 'Falta de marcação', 'Cartão Amarelo', 9),
    (85, 'Palmeiras', 'Felipe Melo', 'Entrada forte', 'Cartão Amarelo', 9),
    (45, 'Atlético Mineiro', 'Réver', 'Falta tática', 'Cartão Amarelo', 10),
    (60, 'São Paulo', 'Igor Gomes', 'Falta técnica', 'Cartão Amarelo', 10);
