from Persistencia import leitor_queries
from Model import model

class LeitorController:
    def __init__(self, db_path):
        self.leitor = leitor_queries.LeitorQueries(db_path)

    def buscar_informacoes_campeonato(self):
        campeonato = self.leitor.search_league_info()
        if campeonato:
            # Lógica para processar os dados do campeonato, se necessário
            return campeonato
        else:
            return "Campeonato não encontrado."

    def alterar_senha(self, user_id, new_password):
        if self.leitor.change_password(user_id, new_password):
            return "Senha alterada com sucesso."
        else:
            return "Erro ao alterar a senha."

    def listar_campeonatos(self):
        campeonatos = self.leitor.retorna_campeonatos()
        if campeonatos:
            return campeonatos
        else:
            return "Nenhum campeonato encontrado."

    def listar_times(self):
        times = self.leitor.retorna_times()

        #vem uma lista de tuplas, preciso converter para uma lista de dicionários
        lista_times = []
        for tupla in times:
            dicionario = {
                "nome": tupla[0],
                "vitorias": tupla[1],
                "derrotas": tupla[2],
                "empates": tupla[3],
                "pontos": tupla[1]*3 + tupla[3]
            }
            lista_times.append(dicionario)

        if times:
            return lista_times
        else:
            print("Nenhum time encontrado.")
            return False
