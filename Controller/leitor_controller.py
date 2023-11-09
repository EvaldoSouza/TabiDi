from Usuarios.user import UserPrivilege
from Persistencia import leitor_queries

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
        if times:
            return times
        else:
            return "Nenhum time encontrado."
