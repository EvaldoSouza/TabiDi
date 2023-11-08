from Persistencia import admin_queries

class AdminController:
    def __init__(self, db_path):
        self.admin_model = admin_queries.AdminModel(db_path)

    def consultar_todos_usuario(self):
        return self.admin_model.consultar_todos_usuario()

    def pesquisar_usuario(self, user_id):
        return self.admin_model.pesquisar_usuario(user_id)

    def deletar_usuario(self, user_id):
        return self.admin_model.deletar_usuario(user_id)

    def update_nome(self, user_id, new_nome):
        return self.admin_model.update_nome(user_id, new_nome)

    def update_email(self, user_id, new_email):
        return self.admin_model.update_email(user_id, new_email)

    def update_senha(self, user_id, new_senha):
        return self.admin_model.update_senha(user_id, new_senha)

    def update_privilegio(self, user_id, new_privilegio):
        return self.admin_model.update_privilegio(user_id, new_privilegio)

    def close_connection(self):
        self.admin_model.close_connection()
