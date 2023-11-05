import sqlite3

class Leitor:
    def __init__(self, db_path, nome):
        self.db_path = db_path
        self.nome = nome
        self.leitor_id = self.obter_leitor_id()
        if self.leitor_id is None:
            raise ValueError("Usuário não encontrado")

        self.create_table()

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

    def create_table(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(f'''
                    CREATE TABLE IF NOT EXISTS parametros_busca_{self.leitor_id} (
                        parametros TEXT,
                        PRIMARY KEY (parametros)
                    )
                ''')
        except Exception as e:
            print(f"Erro ao criar tabela de parâmetros de busca: {e}")

    def save_search_params(self, parametros):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(f"INSERT OR REPLACE INTO parametros_busca_{self.leitor_id} (parametros) VALUES (?)", (parametros,))
                conn.commit()
                return True
        except Exception as e:
            print(f"Erro ao salvar os parâmetros de busca: {e}")
            return False

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
