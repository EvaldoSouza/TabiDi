class User():
    def __init__(self, nome, senha, email, privilegio) -> None:
        self.nome = nome
        self.senha = senha
        self.email = email
        self.privilegio = privilegio

class Campeonato:
    def __init__(self, nome, ano) -> None:
        self.nome = nome
        self.ano = ano

class Time:
    def __init__(self, nome_principal, complemento, tecnico, estadio, cidade, vitorias=0, empates=0, derrotas=0):
        self.nome_principal = nome_principal
        self.complemento = complemento
        self.tecnico = tecnico
        self.estadio = estadio
        self.cidade = cidade
        self.vitorias = vitorias
        self.empates = empates
        self.derrotas = derrotas

    def pontos(self):
        self.pontos = self.vitorias*3 + self.empates
        return self.pontos

class Partida:
    def __init__(self, mandante_nome, mandante_complemento, visitante_nome, visitante_complemento, rodada, data_hora, arbitros, local):
        self.mandante_nome = mandante_nome
        self.mandante_complemento = mandante_complemento
        self.visitante_nome = visitante_nome
        self.visitante_complemento = visitante_complemento
        self.rodada = rodada
        self.data_hora = data_hora
        self.arbitros = arbitros
        self.local = local

class Jogador:
    def __init__(self, nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc, suspenso=False):
        self.nome = nome
        self.apelido = apelido
        self.posicao = posicao
        self.time_atual_nome = time_atual_nome
        self.time_atual_complemento = time_atual_complemento
        self.times_pass = times_pass
        self.data_nasc = data_nasc
        self.suspenso = suspenso

class Gol:
    def __init__(self, tempo_partida, time_fez_nome, time_levou_nome, jogador_fez, jogador_assis, tipo_gol, fora_de_casa, partida):
        self.tempo_partida = tempo_partida
        self.time_fez_nome = time_fez_nome
        self.time_levou_nome = time_levou_nome
        self.jogador_fez = jogador_fez
        self.jogador_assis = jogador_assis
        self.tipo_gol = tipo_gol
        self.fora_de_casa = fora_de_casa
        self.partida = partida

class Falta:
    def __init__(self, tempo_partida, time_faltoso, participante_faltoso, tipo_falta, cartao, partida):
        self.tempo_partida = tempo_partida
        self.time_faltoso = time_faltoso
        self.participante_faltoso = participante_faltoso
        self.tipo_falta = tipo_falta
        self.cartao = cartao
        self.partida = partida

class Joga:
    def __init__(self, nome_jogador, apelido_jogador, posicao_jogador, num_partida, substituicoes_id):
        self.nome_jogador = nome_jogador
        self.apelido_jogador = apelido_jogador
        self.posicao_jogador = posicao_jogador
        self.num_partida = num_partida
        self.substituicoes_id = substituicoes_id

class TimesPass:
    def __init__(self, nome_jogador, apelido_jogador, nome_time):
        self.nome_jogador = nome_jogador
        self.apelido_jogador = apelido_jogador
        self.nome_time = nome_time

class Substituicoes:
    def __init__(self, nome_jogador_entra, apelido_jogador_entra, nome_jogador_sai, apelido_jogador_sai, tempo_partida, num_partida):
        self.nome_jogador_entra = nome_jogador_entra
        self.apelido_jogador_entra = apelido_jogador_entra
        self.nome_jogador_sai = nome_jogador_sai
        self.apelido_jogador_sai = apelido_jogador_sai
        self.tempo_partida = tempo_partida
        self.num_partida = num_partida
