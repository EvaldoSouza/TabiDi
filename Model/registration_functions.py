import sqlite3
from Controller.user import UserPrivilege

#TODO tratar os dados aqui...se for uma boa ideia
def register_user(username, email, password):
        conn = sqlite3.connect('db_usuario.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario WHERE nome = ?", (username))
        user = cursor.fetchone() #retorna uma lista de informações
        #checando se o usuario ja existe
        if user:
            #se o usuario ja existe, retorna falso
            return False
        else:
            cursor.execute("INSERT INTO users (username, email, password, privilege) VALUES (?, ?, ?, ?)", (username, email, password, UserPrivilege.LER.value))
            conn.commit()
            return True