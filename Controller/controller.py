from View import view
from Model import model

class Controller:
    def __init__(self):
        self.model = model.Model("TabeDi")
        self.view = view.View(self)

    def main_controller(self):
        #self.model.main_model() #preciso colocar um metodo main no model...como?
        self.view.main_view()
    
    def checar_credenciais(self, usuario, senha):
        #FAZER UM TRATAMENTO DA VALIDADE DOS DADOS, COMO TAMANHO E CARACTERES ESPECIAIS --Evaldo
        return self.model.check_credentials(usuario,senha)

    def registrar_novo_usuario(self,username, password):
        #FAZER UM TRATAMENTO DA VALIDADE DOS DADOS, COMO TAMANHO E CARACTERES ESPECIAIS --Evaldo
        return self.model.register_user(username, password)
    
    def fechar_database(self):
        #DESCOBRIR ONDE PRECISA FECHAR O BANCO DE DADOS --Evaldo
        self.model.close()