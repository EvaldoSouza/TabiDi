#Classe para definir qual o tipo do usuário, e chamar os controllers corretos
from Persistencia import user_queries
#Ta inutil essa desgraça
class UserController():

    def consultar_privilegio(self, nome):
        return user_queries.consultar_privilegio(nome)
    
    def consultar_email(self, nome):
        return user_queries.consultar_email(nome)

