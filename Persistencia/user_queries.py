#Model com as funções básicas do usuário com relação a ele mesmo, como alterar senha e email
import sqlite3

#tentando fazer sem criar classe por enquanto
def consultar_privilegio(nome):
    try:
        with sqlite3.connect("Database/db_usuarios.sqlite") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT privilegio FROM USUARIO WHERE nome = ?", (nome,))
            privilegio = cursor.fetchone()
            if privilegio:
                return privilegio
            else:
                return None
    except Exception as e:
            print(f"Erro ao obter o leitor_id: {e}")
            return None

def consultar_email(nome):
    try:
        with sqlite3.connect("Database/db_usuarios.sqlite") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT email FROM USUARIO WHERE nome = ?", (nome,))
            email = cursor.fetchone()
            if email:
                return email
            else:
                return None
    except Exception as e:
            print(f"Erro ao obter o leitor_id: {e}")
            return None
    

def change_password( user_id, new_password):
        try:
            with sqlite3.connect("Database/db_usuarios.sqlite") as conn: #sempre vai consultar na mesma base
                cursor = conn.cursor()
                cursor.execute("UPDATE USUARIO SET senha = ? WHERE nome = ?", (new_password, user_id))
                conn.commit()
                return True
        except Exception as e:
            print(f"Erro ao alterar a senha: {e}")
            return False