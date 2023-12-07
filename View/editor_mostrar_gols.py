import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.messagebox import showinfo
from Controller import editor_controller


class EditorMostrarGols(tk.Toplevel): 
    def __init__(self, root, db_path, partida_num):
        super().__init__(root)
        self.db_path = db_path

        self.partida_num = partida_num


        self.controller = editor_controller.EditorController(self.db_path)
        #Geometria básica
        self.geometry("900x600")
        self.resizable(width="TRUE", height="TRUE")

                        # Adicionando um logotipo
        self.logo_image = PhotoImage(file="View/img/logo.png")
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.place(relx=0.5, rely=0.15, anchor="center")

        self.button1 = tk.Button(self, text="Adicionar Gol", command=self.adicionar_gol, bg="green", fg="black", font=("Arial", 14))
        self.button1.pack(side=tk.RIGHT, padx=10)

        self.button1 = tk.Button(self, text="Deletar Gol", command=self.deletar_gol, bg="red", fg="black", font=("Arial", 14))
        self.button1.pack(side=tk.RIGHT, padx=10)

        self.tabela_gols = self.construir_tabela_gols(self.lista_gols())
        self.tabela_gols.pack(side=tk.LEFT, padx=10)

        # Configuração de estilo para os elementos da interface
        self.label_tempo = tk.Label(self, text="Tempo de Partida:", bg="#F0F0F0", font=("Arial", 12))
        self.label_time_fez = tk.Label(self, text="Time que Fez:", bg="#F0F0F0", font=("Arial", 12))
        self.label_time_levou = tk.Label(self, text="Time que Levou:", bg="#F0F0F0", font=("Arial", 12) )
        self.label_jogador = tk.Label(self, text="Jogador que Fez:", bg="#F0F0F0", font=("Arial", 12) )
        #self.label_cidade = tk.Label(self, text="Cidade:", bg="#F0F0F0", font=("Arial", 12) )

        # Usar StringVar é uma forma mais gerenciável e clara de lidar com inputs e objetos desse tipo
        self.tempo_var = tk.StringVar()
        self.time_fez_var = tk.StringVar()
        self.time_levou_var = tk.StringVar()
        self.jogador_var = tk.StringVar()
        #self.cidade_var = tk.StringVar()

        self.entry_tempo = tk.Entry(self, font=("Arial", 14), textvariable=self.tempo_var)
        self.entry_time_fez = tk.Entry(self, font=("Arial", 14), textvariable=self.time_fez_var)
        self.entry_time_levou = tk.Entry(self, font=("Arial", 14), textvariable=self.time_levou_var)
        self.entry_jogador = tk.Entry(self, font=("Arial", 14), textvariable=self.jogador_var)
        #self.entry_cidade = tk.Entry(self, font=("Arial", 14), textvariable=self.cidade_var)

        # Centralizando as labels
        self.label_tempo.place(relx=0.1, rely=0.7, anchor="center")
        self.label_time_fez.place(relx=0.1, rely=0.8, anchor="center")
        self.label_time_levou.place(relx=0.1, rely=0.9, anchor="center")
        self.label_jogador.place(relx=0.1, rely=0.95, anchor="center")
        #self.label_cidade.place(relx=0.3, rely=0.7, anchor="center")

        # Posicionamento dos campos de entrada
        self.entry_tempo.place(relx=0.2, rely=0.7, anchor="center")
        self.entry_time_fez.place(relx=0.2, rely=0.8, anchor="center")
        self.entry_time_levou.place(relx=0.2, rely=0.9, anchor="center")
        self.entry_jogador.place(relx=0.2, rely=0.95, anchor="center")
        #self.entry_cidade.place(relx=0.5, rely=0.7, anchor="center")
    

    
    def construir_tabela_gols(self, lista_gols):

        colunas = ("tempo", "time_fez", "time_levou", "jogador_fez")
        tabela = ttk.Treeview(self, columns=colunas, show='headings')
        tabela.heading("tempo", text="tempo")
        tabela.heading("time_fez", text="time_fez")
        tabela.heading("time_levou", text="time_levou")
        tabela.heading("jogador_fez", text="jogador_fez")
        

        for partida in lista_gols:
            # Insert a new item with the "nome" and "time_fez" values
            tabela.insert("", "end", values=(partida))
        
        tabela.bind('<<TreeviewSelect>>', self.gol_selecionada)
        #self.tabela.bind("<ButtonPress>", self.exemplo_item_selecionado_evento)
        
        #self.tabela.pack() #provavelmente vou ter que retornar o objeto, e dar o pack fora da função
        return tabela
    
    def gol_selecionada(self, event):
        #como são duas tabelas, vai er que mudar a logica
        time_selecionado = self.tabela_gols.selection()
        if time_selecionado:
            self.gol = self.tabela_gols.item(time_selecionado)["values"]


    def lista_gols(self):
        lista = self.controller.listar_gols(self.partida_num)
        return lista
    
    def adicionar_gol(self):
        tempo = self.entry_tempo.get()
        time_fez = self.entry_time_fez.get()
        time_levou = self.entry_time_levou.get()
        jogador = self.entry_jogador.get()

        if self.controller.criar_gol(tempo, time_fez, time_levou, jogador, "", "", "", self.partida_num):
            print("Gol inserido com sucesso")

    def deletar_gol(self):
        self.controller.excluir_partida(self.gol[0])
        print("Deletando partida ", self.gol[0])
        # self.tabela_partidas.delete(*self.tabela_partidas.get_children())
        # self.tabela_partidas = self.construir_tabela_partidas(self.lista_partidas())

    def mostrar_gols(self):
        gols = EditorMostrarGols(self, self.db_path)
        gols.mainloop()