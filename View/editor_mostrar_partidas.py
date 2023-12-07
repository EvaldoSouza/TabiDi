import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.messagebox import showinfo
from Controller import editor_controller
from .editor_mostrar_gols import EditorMostrarGols


class EditorMostrarPartidas(tk.Toplevel): 
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

        # self.button1 = tk.Button(self, text="Adicionar Gol", command=self.adicionar_gol, bg="green", fg="black", font=("Arial", 14))
        # self.button1.pack(side=tk.RIGHT, padx=10)
        self.button1 = tk.Button(self, text="Mostrar Gols", command=self.mostrar_gols, bg="green", fg="black", font=("Arial", 14))
        self.button1.pack(side=tk.BOTTOM, padx=10)
        self.button1 = tk.Button(self, text="Deletar Partida", command=self.deletar_partida, bg="red", fg="black", font=("Arial", 14))
        self.button1.pack(side=tk.BOTTOM, padx=10)

        self.tabela_partidas = self.construir_tabela_partidas(self.lista_partidas())
        self.tabela_partidas.pack(side=tk.LEFT, padx=10)
    

    
    def construir_tabela_partidas(self, lista_partidas):

        colunas = ("mandante", "complemento", "visitante", "complemento_v")
        tabela = ttk.Treeview(self, columns=colunas, show='headings')
        tabela.heading("mandante", text="Nome")
        tabela.heading("complemento", text="Complemento")
        tabela.heading("visitante", text="Visitante")
        tabela.heading("complemento_v", text="Complemento")

        for partida in lista_partidas:
            # Insert a new item with the "nome" and "complemento" values
            tabela.insert("", "end", values=partida[1:])
        
        tabela.bind('<<TreeviewSelect>>', self.partida_selecionada)
        #self.tabela.bind("<ButtonPress>", self.exemplo_item_selecionado_evento)
        
        #self.tabela.pack() #provavelmente vou ter que retornar o objeto, e dar o pack fora da função
        return tabela
    
    def partida_selecionada(self, event):
        #como são duas tabelas, vai er que mudar a logica
        time_selecionado = self.tabela_partidas.selection()
        if time_selecionado:
            self.partida = self.tabela_partidas.item(time_selecionado)["values"]


    def lista_partidas(self):
        lista = self.controller.recuperar_partidas()
        return lista
    

    def deletar_partida(self):
        self.controller.excluir_partida(self.partida[0])
        print("Deletando partida ", self.partida[0])
        # self.tabela_partidas.delete(*self.tabela_partidas.get_children())
        # self.tabela_partidas = self.construir_tabela_partidas(self.lista_partidas())

    def mostrar_gols(self):
        gols = EditorMostrarGols(self, self.db_path, self.partida[0])
        gols.mainloop()