import tkinter as tk
from tkinter import PhotoImage
from Controller import editor_controller

class EditorCriarNovoJogador(tk.Toplevel):
    def __init__(self, time, complemento, db_path):
        super().__init__()
        self.db_path = db_path
        self.time = time
        self.complemento = complemento
        # Geometria básica
        self.geometry("900x600")
        self.title("Editor - Novo Time")
        self.resizable(width="FALSE", height="FALSE")

        # Adicionando um logotipo
        self.logo_image = PhotoImage(file="View/img/logo.png")
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.place(relx=0.5, rely=0.15, anchor="center")

        # Configuração de estilo para os elementos da interface
        self.label_nome = tk.Label(self, text="Nome:", bg="#F0F0F0", font=("Arial", 12))
        self.label_apelido = tk.Label(self, text="Apelido:", bg="#F0F0F0", font=("Arial", 12))
        self.label_posicao = tk.Label(self, text="Posicao:", bg="#F0F0F0", font=("Arial", 12) )
        self.label_data_nasc = tk.Label(self, text="Data de Nascimento:", bg="#F0F0F0", font=("Arial", 12) )
        #self.label_cidade = tk.Label(self, text="Cidade:", bg="#F0F0F0", font=("Arial", 12) )

        # Usar StringVar é uma forma mais gerenciável e clara de lidar com inputs e objetos desse tipo
        self.nome_var = tk.StringVar()
        self.apelido_var = tk.StringVar()
        self.posicao_var = tk.StringVar()
        self.data_nasc_var = tk.StringVar()
        #self.cidade_var = tk.StringVar()

        self.entry_nome = tk.Entry(self, font=("Arial", 14), textvariable=self.nome_var)
        self.entry_apelido = tk.Entry(self, font=("Arial", 14), textvariable=self.apelido_var)
        self.entry_posicao = tk.Entry(self, font=("Arial", 14), textvariable=self.posicao_var)
        self.entry_data_nasc = tk.Entry(self, font=("Arial", 14), textvariable=self.data_nasc_var)
        #self.entry_cidade = tk.Entry(self, font=("Arial", 14), textvariable=self.cidade_var)

        # Centralizando as labels
        self.label_nome.place(relx=0.3, rely=0.3, anchor="center")
        self.label_apelido.place(relx=0.3, rely=0.4, anchor="center")
        self.label_posicao.place(relx=0.3, rely=0.5, anchor="center")
        self.label_data_nasc.place(relx=0.3, rely=0.6, anchor="center")
        #self.label_cidade.place(relx=0.3, rely=0.7, anchor="center")

        # Posicionamento dos campos de entrada
        self.entry_nome.place(relx=0.5, rely=0.3, anchor="center")
        self.entry_apelido.place(relx=0.5, rely=0.4, anchor="center")
        self.entry_posicao.place(relx=0.5, rely=0.5, anchor="center")
        self.entry_data_nasc.place(relx=0.5, rely=0.6, anchor="center")
        #self.entry_cidade.place(relx=0.5, rely=0.7, anchor="center")


        self.confirmar_button = tk.Button(self, text="Confirmar", command=self.confirmar, bg="green", fg="white", font=("Arial", 14))
        self.confirmar_button.place(relx=0.40, rely=0.8, anchor="center")


        self.voltar_button = tk.Button(self, text="Voltar", command=self.voltar, bg="blue", fg="white", font=("Arial", 14))
        self.voltar_button.place(relx=0.55, rely=0.8, anchor="center")

        # Mostrar resultado do cadastro do time
        self.resultado_label = tk.Label(self, text="", font=("Arial", 14))
        self.resultado_label.place(relx=0.5, rely=0.9, anchor="center")

    def confirmar(self):
        nome = self.nome_var.get()
        apelido = self.apelido_var.get()
        posicao = self.posicao_var.get()
        data_nasc = self.data_nasc_var.get()
        #cidade = self.cidade_var.get()

        #conferindo se algum campo está vazio
        if nome == '' or apelido == '' :
            self.resultado_label.config(text="Nome ou apelido está vazio", fg="red")
        else: 
            #como fazer se um dos outros tres estiver vazio?
             
            controller = editor_controller.EditorController(self.db_path)
            if controller.criar_jogador(nome, apelido, posicao,self.time, self.complemento, " ",  data_nasc):
                self.resultado_label.config(text="Jogador Cadastrado com sucesso", fg="green")
            else:
                #TODO tratar erros diferentes
                self.resultado_label.config(text="Jogador já existe!", fg="red")

    
    def voltar(self):
        self.destroy()
