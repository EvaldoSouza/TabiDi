import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import Toplevel

class TelaCadastro(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        #Geometria básica
        self.geometry("900x600")
        self.title("Tela Cadastro")
        self.resizable(width="FALSE", height="FALSE")
        
        # Adicionando uma imagem de fundo
        self.background_image = PhotoImage(file="View/img/football_background.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Adicionando um logotipo
        self.logo_image = PhotoImage(file="View/img/logo.png")
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.place(relx=0.5, rely=0.15, anchor="center")
        
        # Configuração de estilo para os elementos da interface
        self.label_username = tk.Label(self, text="Usuário:", bg="#F0F0F0", font=("Arial", 12))
        self.label_email = tk.Label(self, text="Email:", bg="#F0F0F0", font=("Arial", 12))
        self.label_password = tk.Label(self, text="Senha:", bg="#F0F0F0", font=("Arial", 12))

        #Usar stringvar é uma forma mais gerenciavel e clara de se lidar com inputs e objetos desse tipo
        self.username_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.entry_username = tk.Entry(self, font=("Arial", 14), textvariable=self.username_var)
        self.entry_email = tk.Entry(self, font=("Arial", 14), textvariable=self.email_var )
        self.entry_password = tk.Entry(self, show="*", font=("Arial", 14), textvariable=self.password_var)
        
        # Centralizando as labels
        self.label_username.place(relx=0.3, rely=0.3, anchor="center")
        self.label_email.place(relx=0.3, rely=0.4, anchor="center")
        self.label_password.place(relx=0.3, rely=0.5, anchor="center")
        
        # Posicionamento dos campos de entrada
        self.entry_username.place(relx=0.5, rely=0.3, anchor="center")
        self.entry_email.place(relx=0.5, rely=0.4, anchor="center")
        self.entry_password.place(relx=0.5, rely=0.5, anchor="center")
        
        # Botão de voltar
        self.back_button = tk.Button(self, text="Fazer Login", command=self.fechar_tela_cadastro, bg="blue", fg="white", font=("Arial", 14))
        self.back_button.place(relx=0.40, rely=0.6, anchor="center")
        
        # Botão de registro
        self.register_button = tk.Button(self, text="Registrar", command=self.registrar, bg="green", fg="white", font=("Arial", 14))
        self.register_button.place(relx=0.55, rely=0.6, anchor="center")
        
        #Mostrar resultado de Login
        self.resultado_label = tk.Label(self, text="", font=("Arial", 14))
        self.resultado_label.place(relx=0.5, rely=0.7, anchor="center") #Conferir se está no lugar certo --Evaldo
    

    def registrar(self):
        username = self.username_var.get()
        email = self.email_var.get()
        password = self.password_var.get()

        if password == '' or email == '' or username == '':
            self.resultado_label.config(text="Um dos campos está vazio", fg="red")
        elif self.controller: #checa o controller ativo
            if self.controller.registrar_novo_usuario(username,email, password): #tenta registrar um usuario 
                self.resultado_label.config(text="Registro bem-sucedido", fg="green") #se deu certo, mostra que funcionou
            else:
                self.resultado_label.config(text="Usuário já existe", fg="red")#se nao deu, mostra que falhou


    def cadastro_view(self):
        self.title("TaBedi")
        self.mainloop()

    def fechar_tela_cadastro(self):
        self.destroy()
        #self.controller.chama_tela_login()