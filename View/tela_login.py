import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from .tela_cadastro import TelaCadastro
from Controller import user_controller
from Model import model
from View import admin_tela_principal, editor_tela_principal, leitor_tela_principal
from Usuarios import user

class TelaLogin(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        #Geometria básica
        self.title('Tabedi')
        self.geometry("900x600")
        self.resizable(width="FALSE", height="FALSE")
        # Adicionando uma imagem de fundo
        self.background_image = PhotoImage(file="View/img/football_background.png")
        self.background_label = tk.Label(self, image=self.background_image) #se usar self, dá um erro com outras imagens, e se usar Toplevel(), não aparece
        self.background_label.place(relwidth=1, relheight=1)

        # Adicionando um logotipo
        self.logo_image = PhotoImage(file="View/img/logo.png")
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
        self.register_button = tk.Button(self, text="Quero registrar", command=self.tela_registro, bg="blue", fg="white", font=("Arial", 14))
        self.register_button.place(relx=0.55, rely=0.6, anchor="center")

        #Mostrar resultado de Login
        self.resultado_label = tk.Label(self, text="", font=("Arial", 14))
        self.resultado_label.place(relx=0.5, rely=0.7, anchor="center") #Conferir se está no lugar certo --Evaldo

    #exemplo de lógica a ser seguida. Não passar objetos StringVar para o controller, pois são mais apropriados para a interface
    # def enter_button_clicked(self):
    #     if self.tela_main.controller:
    #         self.tela_main.controller.enter_login(self.email_var.get(), self.senha_var())

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
                #se pode tela chamar tela, que eu acho que pode, chamar a tela principal aqui
                self.abrir_janela_usuario(username)
            else:
                self.resultado_label.config(text="Usuario ou Senha Incorretos", fg="red")
        else:
            #TODO FAZER TRATAMENTO DE ERRO, QUANDO CONTROLLER NÃO ESTIVER INICIALIZADO
            self.resultado_label.config(text="Controller Não Inicializado", fg="red")

    def tela_registro(self):
        segunda_janela = TelaCadastro(self.controller)
        segunda_janela.title("Janela de Registro")
        #self.withdraw()
    
    def abrir_janela_usuario(self, nome):
            #temos um problema de design!
            #há botões diferentes para cada tipo de usuário na janela principal
            #fazer três janelas diferentes para resolver isso
            #O user_controller que vai fazer essa lógica
            #e fechar tmb essa janela
            #então essa função não chama outra tela, mas sim um controller
            controller = user_controller.UserController()
            email = controller.consultar_email(nome)
            privilegio = controller.consultar_privilegio(nome)
            usuario = model.User(nome, '*', email, privilegio)
            
            #inicializando a tela com um caso base
            
            tela_usario = leitor_tela_principal.LeitorTelaPrincipal(usuario)
                
            if usuario.privilegio == user.UserPrivilege.EDI:
                tela_usario = editor_tela_principal.EditorTelaPrincipal(usuario)

            elif usuario.privilegio == user.UserPrivilege.ADM:
                tela_usario = admin_tela_principal.AdminTelaPrincipal(usuario)

            #fazer a logica de chamar telas aqui! Não pode ter nada de tela no controller
            tela_usario.mainloop()
            self.fechar_tela_login()

    def login_view(self):
        self.title("TaBedi")
        self.mainloop()

    def fechar_tela_login(self):
        self.destroy()