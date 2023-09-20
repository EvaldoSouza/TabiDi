from View import tela_login, display_users
from Model import model
from Controller import user
#teste

class Controller:
    def __init__(self):
        self.model = model.Model("TabeDi")
        self.tela_login = tela_login.Tela_Login(self)
        #self.display_users = display_users.Display_Users(self, users)
        self.usuario_principal = user.LeitorNC()

    def main_controller(self):
        #self.model.main_model() #preciso colocar um metodo main no model...como?
        self.tela_login.login_view()
    
    def checar_credenciais(self, usuario, senha):
        #TODO FAZER UM TRATAMENTO DA VALIDADE DOS DADOS, COMO TAMANHO E CARACTERES ESPECIAIS --Evaldo
        user_data = self.model.check_credentials(usuario,senha)
        if user_data:
            #gambs do momento, não deve abrir direto a janela de display users!
            #o user é a seguinte estrutura ('ee', 'ee@email', 'ADM')
            print(user_data)
            match user_data[2]:
                case user.UserPrivilege.ADM.value:
                    self.usuario_principal = user.Administrador(user_data[0], user_data[1], self.model)            
                    users = self.buscar_todos_usuarios()
                    self.display_users = display_users.Display_Users(self, users)
                    self.tela_login.fechar_tela_login()
                    self.display_users.main_display_users()

                case user.UserPrivilege.LNC.value:
                    print("LeitorNC Uma janela linda que ainda não existe!")
                
                case user.UserPrivilege.LER.value:
                    print("Leitor Uma janela linda que ainda não existe!")
                
                case user.UserPrivilege.EDI.value:
                    print("Editor Uma janela linda que ainda não existe!")
                case _:
                    print("Algo deu errado")

        else:
            print("Usuário não existe")


    def registrar_novo_usuario(self,username, email, password):
        #TODO FAZER UM TRATAMENTO DA VALIDADE DOS DADOS, COMO TAMANHO E CARACTERES ESPECIAIS --Evaldo
        return self.model.register_user(username, email, password)
    
    def fechar_database(self):
        #BUG DESCOBRIR ONDE PRECISA FECHAR O BANCO DE DADOS --Evaldo
        self.model.close()
    
    def buscar_todos_usuarios(self):
        return self.model.get_all_users()
    
    def adm_pesquisa_usuario(self, username):
        
        #check de sanidade
        if isinstance(self.usuario_principal, user.Administrador):
            resultados = self.usuario_principal.pesquisar_usuario(username)
            self.display_users.contruir_tabela(resultados)

        else:
            #TODO usar try e catch, ou algo similar --Evaldo
            print("Usuário não é ADM!")
    
    def adm_alterar_privilegio(self):
        if hasattr(self.usuario_principal, 'alterar_privilegio'):
            privilegios = user.UserPrivilege.list()
            resposta_janela = self.display_users.mostrar_categorias_usuarios(privilegios) #BUG --Não espera a proxima função!
            print("Controller Resposta janela: ", resposta_janela)
            novo_privilegio = resposta_janela
            self.usuario_principal.alterar_privilegio(novo_privilegio)
        else:
            print("Usuário não pode alterar privilégios!")
