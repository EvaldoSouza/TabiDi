import sqlite3

#preciso que isso seja uma classe? ou só as funções esta bom?
#por enquanto fazer so as  funções
#deve ser executada toda ver que se for tentar logar
def check_credentials(username, password):
        # Connect to the SQLite database
        conn = sqlite3.connect('db_usuario.sqlite')

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario WHERE nome = ?", (username))
        user = cursor.fetchone() #retorna uma lista de informações
        if user:
            #mandando usuário, email, privilégio
            user_data = (user[0], user[1], user[3])
            senha_armazenada = user[2] #TODO senha está na segunda posição da lista?
            if senha_armazenada == password:
                 conn.close()
                 return user_data # retorna todas as infos se a senha estiver correta
            else:
                 #não fechar a coneção se estiver
                 conn.close()
                 return user[0] # retornando apenas o nome em caso de senha incorreta
        else:
            #se não existe, cursor.fetchone() retorna None
            conn.close()
            return -1 # -1 para usuario nao cadastrado