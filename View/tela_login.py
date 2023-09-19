import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from .tela_cadastro import Tela_Cadastro

class Tela_Login(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        #Geometria básica
        self.geometry("900x600")
        self.resizable(width="FALSE", height="FALSE")
        # Adicionando uma imagem de fundo
        self.background_image = PhotoImage(file="View/football_background.png")
        self.background_label = tk.Label(self, image=self.background_image) #se usar self, dá um erro com outras imagens, e se usar Toplevel(), não aparece
        self.background_label.place(relwidth=1, relheight=1)

        # Adicionando um logotipo
        self.logo_image = PhotoImage(file="View/sigma.png")
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.place(relx=0.5, rely=0.2, anchor="center")
        
        # Configuração de estilo para os elementos da interface
        self.label_username = tk.Label(self, text="Usuário:", bg="#F0F0F0", font=("Arial", 12))
        self.label_password = tk.Label(self, text="Senha:", bg="#F0F0F0", font=("Arial", 12))

        #Usar stringvar é uma forma mais gerenciavel e clara de se lidar com inputs e objetos desse tipo
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.entry_username = tk.Entry(self, font=("Arial", 14), textvariable=self.username_var)
        self.entry_password = tk.Entry(self, show="*", font=("Arial", 14), textvariable=self.password_var)
        
        # Centralizando as labels
        self.label_username.place(relx=0.3, rely=0.4, anchor="center")
        self.label_password.place(relx=0.3, rely=0.5, anchor="center")
        
        # Posicionamento dos campos de entrada
        self.entry_username.place(relx=0.5, rely=0.4, anchor="center")
        self.entry_password.place(relx=0.5, rely=0.5, anchor="center")
        
        # Botão de login
        self.login_button = tk.Button(self, text="Login", command=self.login, bg="green", fg="white", font=("Arial", 14))
        self.login_button.place(relx=0.40, rely=0.6, anchor="center")
        
        # Botão de registro
        self.register_button = tk.Button(self, text="Quero registrar", command=self.nova_aba, bg="blue", fg="white", font=("Arial", 14))
        self.register_button.place(relx=0.55, rely=0.6, anchor="center")

        #Mostrar resultado de Login
        self.resultado_label = tk.Label(self, text="", font=("Arial", 14))
        self.resultado_label.place(relx=0.5, rely=0.7, anchor="center") #Conferir se está no lugar certo --Evaldo

    #exemplo de lógica a ser seguida. Não passar objetos StringVar para o controller, pois são mais apropriados para a interface
    def enter_button_clicked(self):
        if self.controller:
            self.controller.enter_login(self.email_var.get(), self.senha_var())
    def registrar(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if password == '' or username == '':
            self.resultado_label.config(text="Um dos campos está vazio", fg="red")
        elif self.controller:
            if self.controller.registrar_novo_usuario(username, password):
                self.resultado_label.config(text="Registro bem-sucedido", fg="green")
            else:
                self.resultado_label.config(text="Usuário já existe", fg="red")

    def login(self):
        #deve chamar o método login do controller, e passar os dados para ele
        #já fazer algum tratamento de dados aqui, principalmente a respeito de campos vazios
        username = self.username_var.get()
        password = self.password_var.get()

        #conferindo se algum campo está vazio
        if password == '' or username == '':
            self.resultado_label.config(text="Um dos campos está vazio", fg="red")
        elif self.controller:
            if self.controller.checar_credenciais(username, password):
                #CHAMAR OUTRA JANELA
                self.resultado_label.config(text="Login deu Certo!", fg="green")

            else:
                self.resultado_label.config(text="Usuario ou Senha Incorretos", fg="red")
        else:
            #FAZER TRATAMENTO DE ERRO, QUANDO CONTROLLER NÃO ESTIVER INICIALIZADO
            self.resultado_label.config(text="Controller Não Inicializado", fg="red")

    def registrar(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if password == '' or username == '':
            self.resultado_label.config(text="Um dos campos está vazio", fg="red")
        elif self.controller:
            if self.controller.registrar_novo_usuario(username, password):
                self.resultado_label.config(text="Registro bem-sucedido", fg="green")
            else:
                self.resultado_label.config(text="Usuário já existe", fg="red")


    def main_view(self):
        self.title("TaBedi")
        self.mainloop()

    def nova_aba(self):
        segunda_janela = Tela_Cadastro(self.controller)
        segunda_janela.title("Segunda Janela")
        #self.withdraw()