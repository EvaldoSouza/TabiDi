import sqlite3

class Model:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.__create_table()

    def __create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           username TEXT UNIQUE NOT NULL,
                           password TEXT NOT NULL)''')
        self.conn.commit()

    def check_credentials(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        if user:
            return True
        else:
            return False

    def register_user(self, username, password):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            # Usuário com mesmo nome já existe
            #tratar usuário como chave primaria é uma boa ideia? --Evaldo
            return False

    def get_all_users(self):
        cursor = self.conn.cursor()

        cursor.execute("SELECT username FROM users")
        return cursor.fetchall()
    
    def close(self):
        self.conn.close()