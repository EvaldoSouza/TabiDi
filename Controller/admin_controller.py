from Usuarios.user import UserPrivilege
from Model.admin_model import Admin_Model as model
#essa oo ta me matando, não sei se devo importar editor e user no admin
#vou pelo mais seguro e mais burro, e não importar nada
#por nequanto Administrador vai ser uma classe "pura"


class Administrador():
    def __init__(self, username, email) -> None:
        self.privilegio = UserPrivilege.ADM
        self.username = username
        self.email = email
    

    #proprios
    def pesquisar_usuario(self, username):

        #recebe uma string
        #chama uma querry do banco
        resultados = model.get_user_by_id(username)
        return resultados
    
    def lista_todos(self):
        resultados = model.get_all_users()
        return resultados
    
    def selecionar_usuario():
        #trazer o método do controller para cá
        pass

    def alterar_privilegio(self, user, novo_privilegio):
        check = model.update_privilegio(user, novo_privilegio)
        if check:
            print("Privilegio alterado com sucesso --admin_control")
        else:
            print("Privilegio nao alterado com sucesso --admin_control")
        
        return check

    def alterar_nome(self, user, novo_nome):
        check = model.update_nome(user, novo_nome)
        if check:
            print("Nome alterado com sucesso --admin_control")
        else:
            print("Nome não alterado com sucesso --admin_control")
        
        return check

    def alterar_email(self, user, novo_email):
        check = model.update_email(user, novo_email)
        if check:
            print("Email alterado com sucesso --admin_control")
        else:
            print("Email não alterado com sucesso --admin_control")
        
        return check

    def alterar_senha(self, user, nova_senha):
        check = model.update_senha(user, nova_senha)
        if check:
            print("Senha alterada com sucesso --admin_control")
        else:
            print("Senha não alterada com sucesso --admin_control")
        
        return check
    
    def deletar_usuario(self, user):
        check = model.delete_user(user)
        if check:
            print("Usuario deletado --admin_control")
        else:
            print("Usuario nao deletado --admin_control")
        
        return check