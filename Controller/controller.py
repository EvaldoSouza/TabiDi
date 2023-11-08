from View import tela_login,tela_cadastro, display_users, tela_user, tela_editor
from Model import model, registration_functions, login_functions
from Controller import user

class Controller:
    def __init__(self):
        self.model = model.Model("Database/db_usuarios.sqlite")
        self.usuario_principal = user.Leitor()
        self.tela_login = tela_login.Tela_Login(self)
        
    def main_controller(self):
        #self.model.main_model() #preciso colocar um metodo main no model...como?
        self.tela_login.login_view()
    
    def camps_controller(self):
        self.tela_lista_camps.vercamp()
        
    def ranking_controller(self):
        self.tela_camp.ranking()
    
    def checar_credenciais(self, usuario, senha):
        #user_data = self.model.check_credentials(usuario,senha)
        user_data = login_functions.check_credentials(usuario, senha)
        if user_data:
            #gambs do momento, não deve abrir direto a janela de display users!
            #o user é a seguinte estrutura ('ee', 'ee@email', 'ADM')
            print(user_data)
            match user_data[2]:
                case user.UserPrivilege.ADM.value:
                    self.usuario_principal = user.Administrador()            
                    users = self.buscar_todos_usuarios()
                    self.display_users = display_users.Display_Users(self, users) #TODO mudar essa referencia para admin_display_users
                    self.tela_login.fechar_tela_login()
                    self.display_users.main_display_users()
                
                case user.UserPrivilege.LER.value:
                    tela_user.Tela_User(self.usuario_principal)
                
                case user.UserPrivilege.EDI.value:
                    tela_editor.Tela_Editor(self.usuario_principal)
                case _:
                    print("Algo deu errado --controller")
            
            return True

        else:
            print("Usuário não existe")
            return False
        
        


    def registrar_novo_usuario(self,username, email, password):
        #TODO FAZER UM TRATAMENTO DA VALIDADE DOS DADOS, COMO TAMANHO E CARACTERES ESPECIAIS --Evaldo
        #chama a função do model. Essa função no model já não funciona mais!
        #return self.model.register_user(username, email, password)

        return registration_functions.register_user(username, email, password)
    
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
            self.display_users.mostrar_categorias_usuarios(privilegios) #eu queria que a função parasse aqui
            print("Teste depois da janela")
            print("Controller Resposta janela: ", self.valor_recebido_de_janela)
            self.usuario_principal.alterar_privilegio(self.valor_recebido_de_janela)
        else:
            print("Usuário não pode alterar privilégios!")
        
        print("SAINDO DO ESCOPO!")

    def recebe_valor_de_janela(self, valor):
        #está sendo alterada em outra janela
        #super gambiarra, mudar depois
        self.valor_recebido_de_janela = valor
        return valor
    
    def show_tela_login(self):
        self.tela_login.login_view()

    def show_tela_cadastro(self):
        self.tela_main.show_frame(tela_cadastro.Tela_Cadastro)
    