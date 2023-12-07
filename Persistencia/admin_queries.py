import sqlite3  # If you're using SQLite

class AdminModel:
    _instance = None

    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)  # Connect to the database
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")

    def __new__(cls, db_path):
      if cls._instance is None:
          cls._instance = super().__new__(cls)
      return cls._instance
    
    def consultar_todos_usuario(self):
        self.cursor.execute("SELECT nome, email, privilegio FROM usuario")
        self.all_users = self.cursor.fetchall()
        return self.all_users #retorna uma lista de dicionarios

    def pesquisar_usuario(self, user_id):
        self.cursor.execute("SELECT nome, email, privilegio FROM usuario WHERE nome = ?", (user_id,))
        self.one_user = self.cursor.fetchall()
        return self.one_user

    def deletar_usuario(self, user_id):
        try:
            self.cursor.execute("DELETE FROM usuario WHERE nome = ?", (user_id,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False

    def update_nome(self, user_id, new_nome):
        try:
            query = "UPDATE usuario SET nome = ? WHERE nome = ?"
            self.cursor.execute(query, (new_nome, user_id))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error updating nome: {e}")
            return False

    def update_email(self, user_id, new_email):
        try:
            query = "UPDATE usuario SET email = ? WHERE nome = ?"
            self.cursor.execute(query, (new_email, user_id))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error updating email: {e}")
            return False

    def update_senha(self, user_id, new_senha):
        try:
            query = "UPDATE usuario SET senha = ? WHERE nome = ?"
            self.cursor.execute(query, (new_senha, user_id))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error updating senha: {e}")
            return False

    def update_privilegio(self, user_id, new_privilegio):
        try:
            query = "UPDATE usuario SET privilegio = ? WHERE nome = ?"
            self.cursor.execute(query, (new_privilegio, user_id))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error updating privilegio: {e}")
            return False

    def close_connection(self):
        # Close the database connection when done
        #TODO fechar a conexão quando sair do programa ou deslogar. Acho que fica aberta!
        self.conn.close()


