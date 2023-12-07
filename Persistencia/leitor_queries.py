import sqlite3

class LeitorQueries:
    _instance = None

    def __init__(self, db_path) -> None:
        self.db_path = db_path

    def __new__(cls, db_path):
      if cls._instance is None:
          cls._instance = super().__new__(cls)
      return cls._instance
        
    def search_league_info(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT parametros FROM parametros_busca_{self.leitor_id}")
                parametros = cursor.fetchone()
                if parametros:
                    parametros = parametros[0]
                    cursor.execute("SELECT * FROM campeonato WHERE " + parametros)
                    campeonato = cursor.fetchall()
                    return campeonato
                else:
                    return None
        except Exception as e:
            print(f"Erro ao buscar informações do campeonato: {e}")
            return None

    def change_password(self, user_id, new_password):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE USUARIO SET senha = ? WHERE nome = ?", (new_password, user_id))
                conn.commit()
                return True
        except Exception as e:
            print(f"Erro ao alterar a senha: {e}")
            return False

    def retorna_campeonatos(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM campeonatos")
                campeonatos = cursor.fetchall()
                return campeonatos
        except Exception as e:
            print(f"Erro ao buscar informações do campeonato: {e}")
            return None
        
    def retorna_times(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT nome_principal, vitorias, empates, derrotas FROM time")
                times = cursor.fetchall()
                return times
        except Exception as e:
            print(f"Erro ao buscar informações dos times: {e}")
            return None
        