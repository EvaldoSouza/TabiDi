#Classe para definir qual o tipo do usuário, e chamar os controllers corretos
from Usuarios import user
from Model import user_model
from View import admin_tela_principal, editor_tela_principal, leitor_tela_principal
from Controller import admin_controller, editor_controller, leitor_controller

#TODO Fazer três janelas diferentes para cada usuario

class UserController():

    def set_infos_usuario(self, nome):
        self.nome = nome
        self.privilegio = self.consultar_privilegio(self.nome)
        self.email = self.consultar_email(self.nome)

    def consultar_privilegio(self, nome):
        return user_model.consultar_privilegio(nome)
    
    def consultar_email(self, nome):
        return user_model.consultar_email(nome)

    def chamar_janela_correspondente(self):
        match self.privilegio:
            case user.UserPrivilege.LER:
                #chamar leitor_tela_principal
                tela = leitor_tela_principal.TelaPrincipal(admin_controller.Administrador(self.nome, self.email))
                tela.mainloop()
                
            case user.UserPrivilege.EDI:
                #chamar editor_tela_principal
                pass
            case user.UserPrivilege.ADM:
                pass
        pass
