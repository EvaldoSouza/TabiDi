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

        self.tabela_mandante = self.construir_tabela_mandante(self.times())
        self.tabela_mandante.pack(side=tk.LEFT, padx=10)

        self.tabela_visitante = self.construir_tabela_visitante(self.times())
        self.tabela_visitante.pack(side=tk.LEFT, padx=10)

        # self.popular_tabela(self.tabela_mandante, self.times())
        # self.popular_tabela(self.tabela_visitante, self.times())

        self.rodada_label = tk.Label(self, text="Rodada", font=("Arial", 14))
        self.rodada_var = tk.StringVar()
        self.rodada_entry = tk.Entry(self, font=("Arial", 14), textvariable=self.rodada_var)
        self.rodada_label.place(relx=0.5, rely=0.7, anchor="center")
        self.rodada_entry.place(relx=0.7, rely=0.7, anchor="center")

        self.data_hora_label = tk.Label(self, text="Data e Hora", font=("Arial", 14))
        self.data_hora_var = tk.StringVar()
        self.data_hora_entry = tk.Entry(self, font=('Arial', 14), textvariable=self.data_hora_var)
        self.data_hora_label.place(relx=0.5, rely=0.8, anchor="center")
        self.data_hora_entry.place(relx=0.7, rely=0.8, anchor="center")

        self.arbitros_label = tk.Label(self, text="Arbitros", font=("Arial", 14))
        self.arbitros_var = tk.StringVar()
        self.arbitros_entry = tk.Entry(self, font=("Arial", 14), textvariable=self.arbitros_var)
        self.arbitros_label.place(relx=0.5, rely=0.9, anchor="center")
        self.arbitros_entry.place(relx=0.7, rely=0.9, anchor="center")

        self.select_button = tk.Button(self, text="Cadastrar", background="green", command=self.cadastrar)
        self.select_button.pack(side=tk.RIGHT, padx=10)


    def popular_tabela(self,tabela, lista):
        for item in lista:
            print(item)
            tabela.insert(tk.END, item)

    def construir_tabela_mandante(self, lista_times):

        colunas = ("nome", "complemento")
        tabela = ttk.Treeview(self, columns=colunas, show='headings')
        tabela.heading("nome", text="Nome")
        tabela.heading("complemento", text="Complemento")

        for time in lista_times:
            # Insert a new item with the "nome" and "complemento" values
            tabela.insert("", "end", values=(time.get("nome"), time.get("complemento")))
        
        tabela.bind('<<TreeviewSelect>>', self.time_selecionado_mandante)
        #self.tabela.bind("<ButtonPress>", self.exemplo_item_selecionado_evento)
        
        #self.tabela.pack() #provavelmente vou ter que retornar o objeto, e dar o pack fora da função
        return tabela


    def construir_tabela_visitante(self, lista_times):

        colunas = ("nome", "complemento")
        tabela = ttk.Treeview(self, columns=colunas, show='headings')
        tabela.heading("nome", text="Nome")
        tabela.heading("complemento", text="Complemento")

        for time in lista_times:
            # Insert a new item with the "nome" and "complemento" values
            tabela.insert("", "end", values=(time.get("nome"), time.get("complemento")))
        
        tabela.bind('<<TreeviewSelect>>', self.time_selecionado_visitante)
        #self.tabela.bind("<ButtonPress>", self.exemplo_item_selecionado_evento)
        
        #self.tabela.pack() #provavelmente vou ter que retornar o objeto, e dar o pack fora da função
        return tabela
    
    def cadastrar(self):
        mandante = self.time_mandante
        visitante = self.time_visitante
        data_hora = self.data_hora_entry.get()
        rodada = self.rodada_entry.get()
        arbitros = self.arbitros_entry.get()

        if mandante and visitante and data_hora and rodada:
            self.controller.criar_partida(mandante[0], mandante[1], visitante[0], visitante[1], rodada, data_hora, arbitros, "")
        else:
            #TODO colocar mensagem na tela!
            print("falta um importante")
    

    def inserir_item(self,tabela, item):
        tabela.insert('', 'end', text='1', values=item)

    def time_selecionado_mandante(self, event):
        #como são duas tabelas, vai er que mudar a logica
        time_selecionado = self.tabela_mandante.selection()
        if time_selecionado:
            self.time_mandante = self.tabela_mandante.item(time_selecionado)["values"]

    
    def time_selecionado_visitante(self, event):
        #como são duas tabelas, vai er que mudar a logica
        time_selecionado = self.tabela_visitante.selection()
        if time_selecionado:
            self.time_visitante = self.tabela_visitante.item(time_selecionado)["values"]

    
    def times(self):
        return self.controller.recuperar_times()
    
