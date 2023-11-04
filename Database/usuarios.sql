--Preciso de uma para o campeonato e outra para os usuarios!
CREATE TABLE IF NOT EXISTS USUARIO (
    nome TEXT PRIMARY KEY NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
    privilegio INTEGER DEFAULT 0 --0 Leitor, 1 Editor, 2 Administrador?
);

INSERT INTO USUARIO (nome, email, senha, privilegio) VALUES ('admin', 'admin@email.com', 'admin', 2); --criando um usuario admin base