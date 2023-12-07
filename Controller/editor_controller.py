from Persistencia import editor_queries
import sqlite3
import os
class EditorController:
    def __init__(self, db_file):
        self.editor_queries = editor_queries.EditorQueries(db_file)

    # CRUD para Time
    def criar_time(self, nome_principal, complemento, tecnico, estadio, cidade):
        return self.editor_queries.criar_time(nome_principal, complemento, tecnico, estadio, cidade)

    def recuperar_times(self):
        times = self.editor_queries.recuperar_times()
        #vem uma lista de tuplas, preciso converter para uma lista de dicionários
        lista_times = []
        for tupla in times:
            dicionario = {
                "nome": tupla[0],
                "complemento": tupla[1],
                "vitorias": tupla[2],
                "derrotas": tupla[3],
                "empates": tupla[4],
                "pontos": tupla[2]*3 + tupla[4]
            }
            lista_times.append(dicionario)

        if times:
            return lista_times
        else:
            print("Nenhum time encontrado.")
            return False

    def atualizar_time(self, nome_principal, complemento, novas_vitorias, novos_empates, novas_derrotas):
        return self.editor_queries.atualizar_time(nome_principal, complemento, novas_vitorias, novos_empates, novas_derrotas)

    def excluir_time(self, nome_principal, complemento):
        return self.editor_queries.excluir_time(nome_principal, complemento)

    # CRUD para Partida
    def criar_partida(self, mandante_nome, mandante_complemento, visitante_nome, visitante_complemento, rodada, data_hora, arbitros, local):
        return self.editor_queries.criar_partida(mandante_nome, mandante_complemento, visitante_nome, visitante_complemento, rodada, data_hora, arbitros, local)

    def recuperar_partidas(self):
        return self.editor_queries.recuperar_partidas()

    def atualizar_partida(self, num_partida, novo_rodada, novo_data_hora, novos_arbitros, novo_local):
        return self.editor_queries.atualizar_partida(num_partida, novo_rodada, novo_data_hora, novos_arbitros, novo_local)

    def excluir_partida(self, num_partida):
        return self.editor_queries.excluir_partida(num_partida)

    def fechar_conexao(self):
        self.editor_queries.fechar_conexao()

    # CRUD para Campeonatos
    def criar_campeonato(self, nome, ano):
        camp_file = "Database/Campeonatos/"+nome + ".sqlite" #fazendo o caminho para o arquivo
        #camp_path = os.path.join("Database/", camp_file )
        
        if self.editor_queries.criar_campeonato(nome, ano):
            try:
                with open(camp_file, 'x') as novo: #isso funciona em windows?
                    print("Arquivo criado com sucesso")
            except FileExistsError:
                    print(f"Error: Database '{nome}' already exists.")
                    return False
                
            with open("Database/campeonato.sql", 'r') as file:
                sql_script = file.read()
            
            connection = sqlite3.connect(camp_file)
            cursor = connection.cursor()

            cursor.executescript(sql_script)
            connection.commit()
            connection.close()
            
            return True
        
        else:
            return False


    def recuperar_campeonatos(self):
        return self.editor_queries.recuperar_campeonatos()

    def atualizar_campeonato(self, nome, novo_ano):
        return self.editor_queries.atualizar_campeonato(nome, novo_ano)

    def excluir_campeonato(self, nome):
        if self.editor_queries.excluir_campeonato(nome):
            os.remove("Database/Campeonatos/"+nome + ".sqlite")
            return True
        else:
            return False
        
    #funções de jogador
    def criar_jogador(self, nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc):
        return self.editor_queries.criar_jogador(nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc)
    
    def pesquisar_jogador(self, nome, apelido):
        return self.editor_queries.ler_jogador(nome, apelido)
    
    def pesquisar_qualquer(self, valor):
        return self.editor_queries.get_jogadores_by_partial_key(valor)
    
    def atualizar_jogador(self, nome, apelido, new_posicao, new_time_atual_nome):
        return self.editor_queries.atualizar_jogador(nome, apelido, new_posicao, new_time_atual_nome)
    
    def excluir_jogador(self, nome, apelido):
        return self.editor_queries.excluir_jogador(nome, apelido)
    
    def todos_jogadores_do_time(self, time, complemento):
        return self.editor_queries.todos_jogadores_do_time(time, complemento)

    #funções do gol
    def criar_gol(self, tempo_partida, time_fez_nome, time_levou_nome, jogador_fez, jogador_assis, tipo_gol, fora_de_casa, partida):
        return self.editor_queries.inserir_gol(tempo_partida, time_fez_nome, time_levou_nome, jogador_fez, jogador_assis, tipo_gol, fora_de_casa, partida)
    
    def listar_gols(self, partida):
        return self.editor_queries.obter_gols_partida(partida)
    
    def excluir_gol(self, tempo_partida, time_fez_nome, time_levou_nome, partida):
        return self.editor_queries.excluir_gol(tempo_partida, time_fez_nome, time_levou_nome, partida)



