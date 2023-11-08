import sqlite3

class EditorQueries:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
    
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

    def recuperar_times(self):
        try:
            self.cursor.execute("SELECT nome_principal, complemento, tecnico, estadio, cidade, vitorias, empates, derrotas FROM TIME")
            times = self.cursor.fetchall()
            return times
        except sqlite3.Error as e:
            print(f"Erro ao recuperar times: {e}")

    def atualizar_time(self, nome_principal, complemento, novo_tecnico, novo_estadio, nova_cidade, novas_vitorias, novos_empates, novas_derrotas):
        try:
            self.cursor.execute("UPDATE TIME SET tecnico=?, estadio=?, cidade=?, vitorias=?, empates=?, derrotas=? WHERE nome_principal=? AND complemento=?",
                           (novo_tecnico, novo_estadio, nova_cidade, novas_vitorias, novos_empates, novas_derrotas, nome_principal, complemento))
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

   

    #Fechar banco
    def fechar_conexao(self):
        self.conn.close()


