from Usuarios.user import UserPrivilege
from Model.leitor_model import Leitor as model 

class LeitorController:
    def __init__(self, username, email) -> None:
        self.privilegio = UserPrivilege.LEITOR
        self.username = username
        self.email = email

    def salvar_parametros_busca(self, leitor_id, parametros):
        check = model.save_search_params(leitor_id, parametros)
        if check:
            print("Parâmetros de busca salvos com sucesso")
        else:
            print("Erro ao salvar parâmetros de busca")
        return check

    def buscar_informacoes_campeonato(self, leitor_id):
        resultado = model.search_league_info(leitor_id)
        if resultado:
            return resultado
        else:
            print("Erro ao buscar informações do campeonato")
            return None

    def alterar_senha(self, user_id, nova_senha):
        check = model.change_password(user_id, nova_senha)
        if check:
            print("Senha alterada com sucesso")
        else:
            print("Erro ao alterar a senha")
        return check
