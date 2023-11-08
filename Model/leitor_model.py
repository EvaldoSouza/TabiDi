import sqlite3

class Leitor:
    
    def obter_leitor_id(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT nome FROM USUARIO WHERE nome = ?", (self.nome,))
                usuario = cursor.fetchone()
                if usuario:
                    return self.nome
                else:
                    return None
        except Exception as e:
            print(f"Erro ao obter o leitor_id: {e}")
            return None
        
    def set_infos(self, nome, id):
        self.nome = nome
        self.id = id

    def set_db_path(self, path):
        self.db_path = path

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
        