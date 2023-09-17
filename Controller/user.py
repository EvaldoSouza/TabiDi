from enum import Enum
import abc
#Esquecer um pouco do state patter por enquanto!

#definindo os privilégios como um enum
class UserPrivilege(enumerate):
    LNC = "Leitor Não Cadastrado"
    LER = "Leitor"
    EDI = "Editor"
    ADM = "Administrador"


#quando o controller inicializar, ele cria um user, com o privilégio básico
class User(abc.ABC):
    @abc.abstractclassmethod
    def alterar_senha(): pass
    
    @abc.abstractclassmethod
    def pesquisar_campeonato(): pass

    @abc.abstractclassmethod
    def selecionar_campeonato(): pass

    @abc.abstractclassmethod
    def mostrar_tabela_campeonato(): pass

    @abc.abstractclassmethod
    def buscar_info_campeonato(): pass


class LeitorNC(User):
    def __init__(self) -> None:
        self.privilegio = UserPrivilege.LNC
    
    def login(self):
        pass

    def recuperar_senha(self):
        pass

    def registrar(self):
        pass

    def pesquisar_campeonato(self):
        pass

    def selecionar_campeonato(self):
        pass

    def mostrar_tabela_campeonato(self):
        pass

    def buscar_info_campeonato():
        #mostrar a tela de login, se for implementar
        pass

    def alterar_senha():
        #deixar vazio
        pass

class Leitor(User):
    def __init__(self) -> None:
        self.privilegio = UserPrivilege.LER

    def pesquisar_campeonato(self):
        pass

    def selecionar_campeonato(self):
        pass

    def mostrar_tabela_campeonato(self):
        pass

    def buscar_info_campeonato():
        pass

    def alterar_senha():
        pass

    
    #implementar os métodos da interface

class Editor(User):
    def __init__(self) -> None:
        self.privilegio = UserPrivilege.EDI

    #interface
    def pesquisar_campeonato(self):
        pass

    def selecionar_campeonato(self):
        pass

    def mostrar_tabela_campeonato(self):
        pass

    def buscar_info_campeonato():
        pass

    def alterar_senha():
        pass
    
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
    
    #interface
    def pesquisar_campeonato(self):
        pass

    def selecionar_campeonato(self):
        pass

    def mostrar_tabela_campeonato(self):
        pass

    def buscar_info_campeonato():
        pass

    def alterar_senha():
        pass

    #proprios
    def pesquisar_usuario():
        pass
    
    def selecionar_usuario():
        pass

    def alterar_privilegio():
        pass

    def deletar_usuario():
        pass