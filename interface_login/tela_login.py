import tkinter as tk
from tkinter import PhotoImage
from futdata import Datafut

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login de Futebol")
        self.root.geometry("900x600")  
        self.root.resizable(width="FALSE", height="FALSE")
        self.db = Datafut("login.db")
        
        # Adicionando uma imagem de fundo
        self.background_image = PhotoImage(file="football_background.png")
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Adicionando um logotipo
        self.logo_image = PhotoImage(file="luvapai.png")
        self.logo_label = tk.Label(root, image=self.logo_image)
        self.logo_label.place(relx=0.5, rely=0.2, anchor="center")
        
        # Configuração de estilo para os elementos da interface
        self.label_username = tk.Label(root, text="Usuário:", bg="#F0F0F0", font=("Arial", 12))
        self.label_password = tk.Label(root, text="Senha:", bg="#F0F0F0", font=("Arial", 12))
        self.entry_username = tk.Entry(root, font=("Arial", 14))
        self.entry_password = tk.Entry(root, show="*", font=("Arial", 14))
        
        # Centralizando as labels
        self.label_username.place(relx=0.3, rely=0.4, anchor="center")
        self.label_password.place(relx=0.3, rely=0.5, anchor="center")
        
        # Posicionamento dos campos de entrada
        self.entry_username.place(relx=0.5, rely=0.4, anchor="center")
        self.entry_password.place(relx=0.5, rely=0.5, anchor="center")
        
        # Botão de login
        self.login_button = tk.Button(root, text="Login", command=self.login, bg="green", fg="white", font=("Arial", 14))
        self.login_button.place(relx=0.45, rely=0.6, anchor="center")
        
        # Botão de registro
        self.register_button = tk.Button(root, text="Registrar", command=self.register, bg="blue", fg="white", font=("Arial", 14))
        self.register_button.place(relx=0.55, rely=0.6, anchor="center")
        
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Lógica de autenticação usando a classe Database
        if self.db.check_credentials(username, password):
            resultado_label.config(text="Login bem-sucedido", fg="green")
        else:
            resultado_label.config(text="Login falhou", fg="red")

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Verificar se o campo do usuário ou senha está vazio
        if not username or not password:
            resultado_label.config(text="Usuário e senha são obrigatórios", fg="red")
            return

        # Tenta registrar o usuário no banco de dados
        if self.db.register_user(username, password):
            resultado_label.config(text="Registro bem-sucedido", fg="green")
        else:
            resultado_label.config(text="Usuário já existe", fg="red")

    def close_database(self):
        self.db.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    resultado_label = tk.Label(root, text="", font=("Arial", 14))
    resultado_label.place(relx=0.5, rely=0.7, anchor="center")
    root.mainloop()
