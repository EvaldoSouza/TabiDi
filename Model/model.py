import sqlite3
from Controller.user import UserPrivilege

class Model:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.__create_table()

    def __create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           username TEXT UNIQUE NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL, 
                        privilege TEXT)''')
        self.conn.commit()

    def check_credentials(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        if user:
            #mandar o user inteiro ou apenas os métodos necessários?
            #mandando usuário, email, privilégio
            user_data = (user[1], user[2], user[4])
            return user_data
        else:
            #se não existe, cursor.fetchone() retorna None
            return False

    def register_user(self, username, email, password):
        cursor = self.conn.cursor()
        #checando se a tabela está vazia, se estiver, o primeiro usuário registrado é ADM
        cursor.execute("SELECT EXISTS (SELECT 1 FROM users)")
        primeira_linha = cursor.fetchone()
        if primeira_linha[0] == 0:
            print("banco vazio, primeiro usuário adm")
            try:
                cursor.execute("INSERT INTO users (username, email, password, privilege) VALUES (?, ?, ?, ?)", (username, email, password, UserPrivilege.ADM.value))
                self.conn.commit()
                return True
            except sqlite3.IntegrityError:
                # Usuário com mesmo nome já existe
                #tratar usuário como chave primaria é uma boa ideia? --Evaldo
                return False
        else:
            try:
                cursor.execute("INSERT INTO users (username, email, password, privilege) VALUES (?, ?, ?, ?)", (username, email, password, UserPrivilege.LER.value))
                self.conn.commit()
                return True
            except sqlite3.IntegrityError:
                # Usuário com mesmo nome já existe
                #tratar usuário como chave primaria é uma boa ideia? --Evaldo
                return False

    def get_all_users(self):
        cursor = self.conn.cursor()
        #selecionando sem mandar a senha ou indice
        cursor.execute("SELECT username, email, privilege FROM users")
        return cursor.fetchall()
    
    def close(self):
        self.conn.close()
    
    def delete_table(self, table_name):
        cursor = self.conn.cursor()
        cursor.execute("DROP TABLE (?)", table_name)
        print("Tabela ", table_name, " deletada")
    
    def search_user(self, username):
        cursor = self.conn.cursor()
        cursor.execute("SELECT username, email, privilege FROM users WHERE username LIKE ?", ("%"+ username + "%",))
        return cursor.fetchall()
