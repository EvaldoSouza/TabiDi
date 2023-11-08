from Persistencia import editor_queries
class EditorController:
    def __init__(self, db_file):
        self.editor_queries = editor_queries.EditorQueries(db_file)

    # CRUD para Time
    def criar_time(self, nome_principal, complemento, tecnico, estadio, cidade):
        return self.editor_queries.criar_time(nome_principal, complemento, tecnico, estadio, cidade)

    def recuperar_times(self):
        return self.editor_queries.recuperar_times()

    def atualizar_time(self, nome_principal, complemento, novo_tecnico, novo_estadio, nova_cidade, novas_vitorias, novos_empates, novas_derrotas):
        return self.editor_queries.atualizar_time(nome_principal, complemento, novo_tecnico, novo_estadio, nova_cidade, novas_vitorias, novos_empates, novas_derrotas)

    def excluir_time(self, nome_principal, complemento):
        return self.editor_queries.excluir_time(nome_principal, complemento)

    # CRUD para Partida
    def criar_partida(self, mandante_nome, mandante_complemento, visitante_nome, visitante_complemento, rodada, data_hora, arbitros, local):
        return self.editor_queries.criar_partida(mandante_nome, mandante_complemento, visitante_nome, visitante_complemento, rodada, data_hora, arbitros, local)

    def recuperar_partidas(self):
        return self.editor_queries.recuperar_partidas()

    def atualizar_partida(self, num_partida, novo_rodada, novo_data_hora, novos_arbitros, novo_local):
        return self.editor_queries.atualizar_partida(num_partida, novo_rodada, novo_data_hora, novos_arbitros, novo_local)

    def excluir_partida(self, num_partida):
        return self.editor_queries.excluir_partida(num_partida)

    def fechar_conexao(self):
        self.editor_queries.fechar_conexao()
