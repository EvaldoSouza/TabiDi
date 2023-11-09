import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import Toplevel

class Tela_Editor_NovoCamp(tk.Toplevel): #TODO melhorar o nome da classe
    def __init__(self):
        super().__init__()
        #Geometria básica
        self.geometry("900x600")
        self.title("Editor - Novo Campeonato")
        self.resizable(width="FALSE", height="FALSE")

        # Adicionando um logotipo
        self.logo_image = PhotoImage(file="View/img/logo.png")
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.place(relx=0.5, rely=0.15, anchor="center")
        
        # Configuração de estilo para os elementos da interface
        self.label_nome = tk.Label(self, text="Nome:", bg="#F0F0F0", font=("Arial", 12))
        self.label_ano = tk.Label(self, text="Ano:", bg="#F0F0F0", font=("Arial", 12))
        self.label_times = tk.Label(self, text="Times:", bg="#F0F0F0", font=("Arial", 12))

        #Usar stringvar é uma forma mais gerenciavel e clara de se lidar com inputs e objetos desse tipo
        self.nome_var = tk.StringVar()
        self.ano_var = tk.StringVar()
        self.times_var = tk.StringVar()
        self.entry_nome = tk.Entry(self, font=("Arial", 14), textvariable=self.nome_var)
        self.entry_ano = tk.Entry(self, font=("Arial", 14), textvariable=self.ano_var )
        self.entry_times = tk.Entry(self, font=("Arial", 14), textvariable=self.times_var)
        
        # Centralizando as labels
        self.label_nome.place(relx=0.3, rely=0.3, anchor="center")
        self.label_ano.place(relx=0.3, rely=0.4, anchor="center")
        self.label_times.place(relx=0.3, rely=0.5, anchor="center")
        
        # Posicionamento dos campos de entrada
        self.entry_nome.place(relx=0.5, rely=0.3, anchor="center")
        self.entry_ano.place(relx=0.5, rely=0.4, anchor="center")
        self.entry_times.place(relx=0.5, rely=0.5, anchor="center")
        
        # Botão de voltar
        self.adicionar_button = tk.Button(self, text="Adicionar", command=self.adicionar, bg="green", fg="white", font=("Arial", 14))
        self.adicionar_button.place(relx=0.40, rely=0.6, anchor="center")
        
        # Botão de registro
        self.voltar_button = tk.Button(self, text="Voltar", command=self.voltar, bg="blue", fg="white", font=("Arial", 14))
        self.voltar_button.place(relx=0.55, rely=0.6, anchor="center")
        
    def adicionar(self):
      pass

    def voltar(self):
      self.destroy()

    #TODO falta os campos do que isso está alterando, ou pelo menos uma indicação de como isso funciona
    #TODO pegar as informações da tela
    #TODO mandar essas informações para o banco