import sqlite3

class EditorQueries:
    _instance = None
    
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        #self.cursor.execute("PRAGMA foreign_keys = ON") #ta dando erro nas chaves estrangeiras da partida
    
    def __new__(cls, db_path):
      if cls._instance is None:
          cls._instance = super().__new__(cls)
      return cls._instance
    
    #CRUD time
    def criar_time(self, nome_principal, complemento, tecnico, estadio, cidade):
        try:
            self.cursor.execute("INSERT INTO TIME (nome_principal, complemento, tecnico, estadio, cidade) VALUES (?, ?, ?, ?, ?)",
                           (nome_principal, complemento, tecnico, estadio, cidade))
            self.conn.commit()
            print("Time criado com sucesso.")
            return True
        except sqlite3.Error as e:
            print(f"Erro ao criar time: {e}")

    def recuperar_todos_dados_times(self):
        try:
            self.cursor.execute("SELECT nome_principal, complemento, tecnico, estadio, cidade, vitorias, empates, derrotas FROM TIME")
            times = self.cursor.fetchall()
            return times
        except sqlite3.Error as e:
            print(f"Erro ao recuperar times: {e}")

    def recuperar_times(self):
        try:
    
            self.cursor.execute(f"SELECT nome_principal, complemento, vitorias, empates, derrotas FROM TIME")
            times = self.cursor.fetchall()
            return times
        except Exception as e:
            print(f"Erro ao buscar informações dos times: {e}")
            return None

    def atualizar_time(self, nome_principal, complemento, novas_vitorias, novos_empates, novas_derrotas):
        try:
            self.cursor.execute("UPDATE TIME SET vitorias=?, empates=?, derrotas=? WHERE nome_principal=? AND complemento=?",
                           ( novas_vitorias, novos_empates, novas_derrotas, nome_principal, complemento))
            self.conn.commit()
            print("Time atualizado com sucesso.")
            return True
        except sqlite3.Error as e:
            print(f"Erro ao atualizar time: {e}")

    def excluir_time(self, nome_principal, complemento):
        try:
            self.cursor.execute("DELETE FROM TIME WHERE nome_principal=? AND complemento=?", (nome_principal, complemento))
            self.conn.commit()
            print("Time excluído com sucesso.")
            return True
        except sqlite3.Error as e:
            print(f"Erro ao excluir time: {e}")
    #TODO pesquisar time

    #CRUD partida
    def criar_partida(self, mandante_nome, mandante_complemento, visitante_nome, visitante_complemento, rodada, data_hora, arbitros, local):
            try:
                self.cursor.execute("INSERT INTO PARTIDA (mandante_nome, mandante_complemento, visitante_nome, visitante_complemento, rodada, data_hora, arbitros, local) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                            (mandante_nome, mandante_complemento, visitante_nome, visitante_complemento, rodada, data_hora, arbitros, local))
                self.conn.commit()
                print("Partida criada com sucesso.")
                return True
            except sqlite3.Error as e:
                print(f"Erro ao criar partida: {e}")

    def recuperar_partidas(self):
        try:
            self.cursor.execute("SELECT num_partida, mandante_nome, mandante_complemento, visitante_nome, visitante_complemento, rodada, data_hora, arbitros, local FROM PARTIDA")
            partidas = self.cursor.fetchall()
            return partidas
        except sqlite3.Error as e:
            print(f"Erro ao recuperar partidas: {e}")

    #TODO pesquisar uma única partida
    def atualizar_partida(self, num_partida, novo_rodada, novo_data_hora, novos_arbitros, novo_local):
        try:
            self.cursor.execute("UPDATE PARTIDA SET rodada=?, data_hora=?, arbitros=?, local=? WHERE num_partida=?",
                           (novo_rodada, novo_data_hora, novos_arbitros, novo_local, num_partida))
            self.conn.commit()
            print("Partida atualizada com sucesso.")
            return True
        except sqlite3.Error as e:
            print(f"Erro ao atualizar partida: {e}")

    def excluir_partida(self, num_partida):
        try:
            self.cursor.execute("DELETE FROM PARTIDA WHERE num_partida=?", (num_partida,))
            self.conn.commit()
            print("Partida excluída com sucesso.")
            return True
        except sqlite3.Error as e:
            print(f"Erro ao excluir partida: {e}")

   #CRUD Campeonato
    def criar_campeonato(self, nome, ano):
        try:
            self.cursor.execute("INSERT INTO CAMPEONATOS (nome, ano) VALUES (?, ?)", (nome, ano))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao criar campeonato: {e}")
            return False

    def recuperar_campeonatos(self):
        try:
            self.cursor.execute("SELECT nome, ano FROM CAMPEONATOS")
            campeonatos = self.cursor.fetchall()
            return campeonatos
        except sqlite3.Error as e:
            print(f"Erro ao recuperar campeonatos: {e}")

    def atualizar_campeonato(self, nome, novo_ano):
        try:
            self.cursor.execute("UPDATE CAMPEONATOS SET ano=? WHERE nome=?", (novo_ano, nome))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao atualizar campeonato: {e}")
            return False

    def excluir_campeonato(self, nome):
        try:
            self.cursor.execute("DELETE FROM CAMPEONATOS WHERE nome=?", (nome,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao excluir campeonato: {e}")
            return False

    #CRUD jogador
    def criar_jogador(self, nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc):
            try:
                self.cursor.execute("""
                    INSERT INTO JOGADOR 
                    (nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc) 
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (nome, apelido, posicao, time_atual_nome, time_atual_complemento, times_pass, data_nasc))
                self.conn.commit()
                return True
            except sqlite3.Error as e:
                print(f"Erro ao criar jogador: {e}")
                return False

    def ler_jogador(self, nome, apelido):
        try:
            self.cursor.execute("""
                SELECT * FROM JOGADOR 
                WHERE nome = ? AND apelido = ?
            """, (nome, apelido))
            jogador = self.cursor.fetchone()
            return jogador
        except sqlite3.Error as e:
            print(f"Erro ao ler jogador: {e}")
            return None

    def atualizar_jogador(self, nome, apelido, new_posicao, new_time_atual_nome):
        try:
            self.cursor.execute("""
                UPDATE JOGADOR 
                SET posicao = ?, time_atual_nome = ? 
                WHERE nome = ? AND apelido = ?
            """, (new_posicao, new_time_atual_nome, nome, apelido))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao atualizar jogador: {e}")
            return False

    def excluir_jogador(self, nome, apelido):
        try:
            self.cursor.execute("""
                DELETE FROM JOGADOR 
                WHERE nome = ? AND apelido = ?
            """, (nome, apelido))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao excluir jogador: {e}")
            return False
        
    def todos_jogadores_do_time(self, time, complemento):
        try:
            self.cursor.execute("SELECT * FROM JOGADOR WHERE time_atual_nome = ? and time_atual_complemento = ?", (time, complemento))
            jogadores = self.cursor.fetchall()
            return jogadores
        except sqlite3.Error as e:
            print(f"Erro ao obter jogadores por time: {e}")
            return None
        
    def get_jogadores_by_partial_key(self, partial_key):
        try:
            self.cursor.execute('''
                SELECT * FROM JOGADOR 
                WHERE nome LIKE ? OR apelido LIKE ?
            ''', (f'%{partial_key}%', f'%{partial_key}%'))

            jogadores = self.cursor.fetchall()
            return jogadores
        except sqlite3.Error as e:
            print(f"Erro ao obter jogador por chave primária: {e}")
            return None

    #CRUD do Gol
    def inserir_gol(self, tempo_partida, time_fez_nome, time_levou_nome, jogador_fez, jogador_assis, tipo_gol, fora_de_casa, partida):
        try:
            self.cursor.execute('''
                INSERT INTO GOL 
                (tempo_partida, time_fez_nome, time_levou_nome, jogador_fez, jogador_assis, tipo_gol, fora_de_casa, partida) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (tempo_partida, time_fez_nome, time_levou_nome, jogador_fez, jogador_assis, tipo_gol, fora_de_casa, partida))
            
            return True
        except sqlite3.Error as e:
            print(f"Erro ao inserir gol: {e}")
            return False
        
    def obter_gols_partida(self, num_partida):
        try:
            self.cursor.execute('''
                SELECT * FROM GOL 
                WHERE partida = ?
            ''', (num_partida,))

            gols = self.cursor.fetchall()
            return gols
        except sqlite3.Error as e:
            print(f"Erro ao obter gols da partida: {e}")
            return None
        
    def atualizar_gol(self, tempo_partida, time_fez_nome, time_levou_nome, jogador_fez, jogador_assis, tipo_gol, fora_de_casa, partida):
        try:
            self.cursor.execute('''
                UPDATE GOL 
                SET jogador_fez=?, jogador_assis=?, tipo_gol=?, fora_de_casa=?
                WHERE tempo_partida=? AND time_fez_nome=? AND time_levou_nome=? AND partida=?
            ''', (jogador_fez, jogador_assis, tipo_gol, fora_de_casa, tempo_partida, time_fez_nome, time_levou_nome, partida))
            
            return True
        except sqlite3.Error as e:
            print(f"Erro ao atualizar gol: {e}")
            return False

    def excluir_gol(self, tempo_partida, time_fez_nome, time_levou_nome, partida):
        try:
            self.cursor.execute('''
                DELETE FROM GOL 
                WHERE tempo_partida=? AND time_fez_nome=? AND time_levou_nome=? AND partida=?
            ''', (tempo_partida, time_fez_nome, time_levou_nome, partida))
            
            return True
        except sqlite3.Error as e:
            print(f"Erro ao excluir gol: {e}")
            return False



    #Fechar banco
    def fechar_conexao(self):
        self.conn.close()


