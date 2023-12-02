#Controla as Views quando ainda não está logado. Responsável pela tela de login e registro

#O que preciso fazer?
# - Chamar a tela de login quando o programa for inicializado
# - Chamar a tela de cadastro quando for clicado o botão
#   - Para isso, chamar a função registration
# - Chamar a tela principal quando o login for bem sucedido
#   -Para isso, chamar a função login 

from Persistencia import login_functions
from View import tela_login
from Persistencia import registration_functions

class ControllerInicial:

    def chama_tela_login(self):
        #A tela login precisa de um controller
        self.tela_login = tela_login.TelaLogin(self)
        self.tela_login.login_view()
    
    def checar_credenciais(self, nome, senha):
        user_info = login_functions.check_credentials(nome, senha)
        #três casos: senha correta, senha incorreta, usuario não cadastrado
        #TODO melhorar os avisos
        if user_info == -1:
            print("Usuário não cadastrado --controller_inicial")
            return False
        elif user_info == 0:
            print("Senha incorreta --controller_inicial")
            return False
        else:
            print("Login de sucesso --controller_inicial")
            return True


    def registrar_novo_usuario(self, nome, email, senha):
        return registration_functions.register_user(nome, email, senha)
