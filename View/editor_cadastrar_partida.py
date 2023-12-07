import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

from Controller import editor_controller

class EditorCadastrarPartida(tk.Toplevel):
    def __init__(self, root, db_path):
        super().__init__(root)
        self.db_path = db_path


        self.controller = editor_controller.EditorController(self.db_path)
        #Geometria básica
        self.geometry("900x600")
        self.resizable(width="TRUE", height="TRUE")

                        # Adicionando um logotipo
        self.logo_image = PhotoImage(file="View/img/logo.png")
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.place(relx=0.5, rely=0.15, anchor="center")

        self.tabela_mandante = self.construir_tabela(self.times())
        self.tabela_mandante.pack(side=tk.LEFT, padx=10)

        self.tabela_visitante = self.construir_tabela(self.times())
        self.tabela_visitante.pack(side=tk.LEFT, padx=10)

        # self.popular_tabela(self.tabela_mandante, self.times())
        # self.popular_tabela(self.tabela_visitante, self.times())

        self.rodada_label = tk.Label(self, text="Rodada", font=("Arial", 14))
        self.rodada_var = tk.StringVar()
        self.rodada_entry = tk.Entry(self, font=("Arial", 14), textvariable=self.rodada_var)
        self.rodada_label.place(relx=0.5, rely=0.4, anchor="center")
        self.rodada_entry.place(relx=0.7, rely=0.4, anchor="center")

        self.data_hora_label = tk.Label(self, text="Data e Hora", font=("Arial", 14))
        self.data_hora_var = tk.StringVar()
        self.data_hora_entry = tk.Entry(self, font=('Arial', 14), textvariable=self.data_hora_var)
        self.data_hora_label.place(relx=0.5, rely=0.5, anchor="center")
        self.data_hora_entry.place(relx=0.7, rely=0.5, anchor="center")

        self.arbitros_label = tk.Label(self, text="Arbitros", font=("Arial", 14))
        self.arbitros_var = tk.StringVar()
        self.arbitros_entry = tk.Entry(self, font=("Arial", 14), textvariable=self.arbitros_var)
        self.arbitros_label.place(relx=0.5, rely=0.6, anchor="center")
        self.arbitros_entry.place(relx=0.7, rely=0.6, anchor="center")

        self.select_button = tk.Button(self, text="Cadastrar", command=self.cadastrar)
        self.select_button.pack(side=tk.RIGHT, padx=10)


    def popular_tabela(self,tabela, lista):
        for item in lista:
            print(item)
            tabela.insert(tk.END, item)

    def construir_tabela(self, lista_times):

        colunas = ("nome", "complemento")
        tabela = ttk.Treeview(self, columns=colunas, show='headings')
        tabela.heading("nome", text="Nome")
        tabela.heading("complemento", text="Complemento")

        for user in lista_times:
            self.inserir_item(tabela, user)
        
        #self.tabela.bind('<<TreeviewSelect>>', self.time_selecionado)
        #self.tabela.bind("<ButtonPress>", self.exemplo_item_selecionado_evento)
        
        #self.tabela.pack() #provavelmente vou ter que retornar o objeto, e dar o pack fora da função
        return tabela

    def cadastrar(self):
        mandante = self.tabela_mandante.get(self.tabela_mandante.curselection())
        visitante = self.tabela_visitante.get(self.tabela_visitante.curselection())
        data_hora = self.data_hora_entry.get()
        rodada = self.rodada_entry.get()
        arbitros = self.arbitros_entry.get()

        if mandante and visitante and data_hora and rodada:
            self.controller.criar_partida(mandante[0], mandante["complemento"], visitante["nome"], visitante["complemento"], rodada, data_hora, arbitros, mandante["estadio"])
            print("partida cadastrada")
        else:
            #TODO colocar mensagem na tela!
            print("falta um importante")
    

    def inserir_item(self,tabela, item):
        tabela.insert('', 'end', text='1', values=item)

    def time_selecionado(self, event):
        #como são duas tabelas, vai er que mudar a logica
        time_selecionado = self.tabela.selection()
        if time_selecionado:
            self.jogador_dados = self.tabela.item(time_selecionado)["values"]
            print(self.jogador_dados)
    
    def times(self):
        return self.controller.recuperar_times()
    
