from enum import Enum
import abc
from Model import model
#Esquecer um pouco do state patter por enquanto!

#definindo os privilégios como um enum
#tentando fazer algo maneiro...não deu certo
class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
class UserPrivilege(ExtendedEnum):
    LER = 0
    EDI = 1
    ADM = 2




#quando o controller inicializar, ele cria um user, com o privilégio básico
#Se a classe herda de abc, e possui um método abstrato, ela já não pode mais ser instanciada
class User(abc.ABC):
    @abc.abstractclassmethod
    def __init__(self) -> None:
        pass
    
    def pesquisar_campeonato(self): pass

    def selecionar_campeonato(self): pass

    def mostrar_tabela_campeonato(self): pass

    def buscar_info_campeonato(self): pass

    def salvar_paramentros_busca(self): pass

    def alterar_senha(self): pass


# class LeitorNC(User):
#     def __init__(self) -> None:
#         self.privilegio = UserPrivilege.LNC
    
#     #Metodos particulares
#     def login(self):
#         pass

#     def recuperar_senha(self):
#         pass

#     def registrar(self):
#         pass

#     #sobrescrevendo, para não fazer nada
#     def buscar_info_campeonato():
#         #mostrar a tela de login, se for implementar
#         pass

#     def alterar_senha():
#         #deixar vazio
#         pass

class Leitor(User):
    def __init__(self) -> None:
        self.privilegio = UserPrivilege.LER

    
    def set_infos(self, username, email):
        self.username = username
        self.email = email
   

class Editor(User):
    def __init__(self) -> None:
        self.privilegio = UserPrivilege.EDI

    
    #proprios
    def cadastrar_campeonato():
        pass

    def deletar_info_camponato():
        pass

    def atualizar_info_campeonato():
        pass

    def inserir_info_campeonato():
        pass
    #nenhum método precisa ser implementado por enquanto, eu acho

class Administrador(Editor, User):
    def __init__(self) -> None:
        self.privilegio = UserPrivilege.ADM
        
    

    def set_infos(self,username, email, db_model):
        self.username = username
        self.email = email
        self.database = db_model

    #proprios
    def pesquisar_usuario(self, username):

        #recebe uma string
        #chama uma querry do banco
        resultados = self.database.search_user(username)
        return resultados
    
    def selecionar_usuario():
        #trazer o método do controller para cá
        pass

    def alterar_privilegio(self, novo_privilegio):
        print("Class ADM, privilegio recebido: ", novo_privilegio)
        #atualizar o banco
        pass

    def deletar_usuario():
        #atualizar o banco
        pass