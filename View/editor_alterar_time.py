import tkinter as tk
from tkinter import PhotoImage
from Controller import editor_controller

class EditorAlterarTime(tk.Toplevel):
    def __init__(self, db_path):
        super().__init__()
        self.geometry("600x300")
        self.resizable(width="TRUE", height="TRUE")
        self.title("Editor - Adicionar Time")

        self.db_path = db_path
        # Adicionando um logotipo
        self.logo_image = PhotoImage(file="View/img/logo.png")
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.place(relx=0.5, rely=0.15, anchor="center")

        # Configuração de estilo para os elementos da interface
        self.label_nome = tk.Label(self, text="Nome:", bg="#F0F0F0", font=("Arial", 12))
        #self.label_pontos = tk.Label(self, text="Pontos:", bg="#F0F0F0", font=("Arial", 12))
        self.label_vitorias = tk.Label(self, text="Vitórias:", bg="#F0F0F0", font=("Arial", 12))
        self.label_derrotas = tk.Label(self, text="Derrotas:", bg="#F0F0F0", font=("Arial", 12))
        self.label_empates = tk.Label(self, text="Empates:", bg="#F0F0F0", font=("Arial", 12))

        # Usar StringVar é uma forma mais gerenciável e clara de lidar com inputs e objetos desse tipo
        self.nome_var = tk.StringVar()
        # self.pontos_var = tk.StringVar()
        self.vitorias_var = tk.StringVar()
        self.derrotas_var = tk.StringVar()
        self.empates_var = tk.StringVar()

        self.entry_nome = tk.Entry(self, font=("Arial", 14), textvariable=self.nome_var)
        # self.entry_pontos = tk.Entry(self, font=("Arial", 14), textvariable=self.pontos_var)
        self.entry_vitorias = tk.Entry(self, font=("Arial", 14), textvariable=self.vitorias_var)
        self.entry_derrotas = tk.Entry(self, font=("Arial", 14), textvariable=self.derrotas_var)
        self.entry_empates = tk.Entry(self, font=("Arial", 14), textvariable=self.empates_var)

        # Centralizando as labels
        self.label_nome.place(relx=0.3, rely=0.3, anchor="center")
        # self.label_pontos.place(relx=0.3, rely=0.4, anchor="center")
        self.label_vitorias.place(relx=0.3, rely=0.5, anchor="center")
        self.label_derrotas.place(relx=0.3, rely=0.6, anchor="center")
        self.label_empates.place(relx=0.3, rely=0.7, anchor="center")

        # Posicionamento dos campos de entrada
        self.entry_nome.place(relx=0.5, rely=0.3, anchor="center")
        # self.entry_pontos.place(relx=0.5, rely=0.4, anchor="center")
        self.entry_vitorias.place(relx=0.5, rely=0.5, anchor="center")
        self.entry_derrotas.place(relx=0.5, rely=0.6, anchor="center")
        self.entry_empates.place(relx=0.5, rely=0.7, anchor="center")

        # Botão de voltar
        self.confirmar_button = tk.Button(self, text="Confirmar", command=self.confirmar, bg="green", fg="white", font=("Arial", 14))
        self.confirmar_button.place(relx=0.40, rely=0.8, anchor="center")

        # Botão de registro
        self.voltar_button = tk.Button(self, text="Voltar", command=self.voltar, bg="blue", fg="white", font=("Arial", 14))
        self.voltar_button.place(relx=0.55, rely=0.8, anchor="center")

        # Mostrar resultado do cadastro do time
        self.resultado_label = tk.Label(self, text="", font=("Arial", 14))
        self.resultado_label.place(relx=0.5, rely=0.9, anchor="center")

    def confirmar(self):
        nome = self.nome_var.get()
        #pontos = self.pontos_var.get()
        vitorias = self.vitorias_var.get()
        derrotas = self.derrotas_var.get()
        empates = self.empates_var.get()

        #conferindo se algum campo está vazio
        if nome == '' or vitorias == '' or derrotas == '' or empates == '': #TODO isso não está bom. Tinha que manter os dados antigos, e só alterar os que mudaram
            self.resultado_label.config(text="Um dos campos está vazio", fg="red")
        else: 
             
            controller = editor_controller.EditorController(self.db_path)
            controller.atualizar_time(nome, nome, vitorias, derrotas, empates)
            self.resultado_label.config(text="Time Cadastrado com sucesso", fg="green")


    
    def voltar(self):
        self.destroy()
