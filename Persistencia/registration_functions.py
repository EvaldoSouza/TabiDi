import sqlite3
from Usuarios.user import UserPrivilege


#por ser uma função, não precisa criar um objeto! Bem legal
def register_user(username, email, password):
        conn = sqlite3.connect('Database/db_usuarios.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario WHERE nome = ?", (username,)) #precisa dessa virgula
        user = cursor.fetchone() #retorna uma lista de informações
        #checando se o usuario ja existe
        if user:
            #se o usuario ja existe, retorna falso
            return False
        else:
            cursor.execute("INSERT INTO usuario (nome, email, senha, privilegio) VALUES (?, ?, ?, ?)", (username, email, password, UserPrivilege.LER.value))
            conn.commit()
            return True