from View import tela_login, display_users
from Model import model

class Controller:
    def __init__(self):
        self.model = model.Model("TabeDi")
        self.tela_login = tela_login.Tela_Login(self)
        #self.display_users = display_users.Display_Users(self, users)

    def main_controller(self):
        #self.model.main_model() #preciso colocar um metodo main no model...como?
        self.tela_login.login_view()
    
    def checar_credenciais(self, usuario, senha):
        #FAZER UM TRATAMENTO DA VALIDADE DOS DADOS, COMO TAMANHO E CARACTERES ESPECIAIS --Evaldo
        if self.model.check_credentials(usuario,senha):
            #gambs do momento, não deve abrir direto a janela de display users!
            users = self.buscar_todos_usuarios()
            self.display_users = display_users.Display_Users(self, users)
            self.tela_login.fechar_tela_login()
            self.display_users.main_display_users()


    def registrar_novo_usuario(self,username, email, password):
        #FAZER UM TRATAMENTO DA VALIDADE DOS DADOS, COMO TAMANHO E CARACTERES ESPECIAIS --Evaldo
        return self.model.register_user(username, email, password)
    
    def fechar_database(self):
        #DESCOBRIR ONDE PRECISA FECHAR O BANCO DE DADOS --Evaldo
        self.model.close()
    
    def buscar_todos_usuarios(self):
        return self.model.get_all_users()