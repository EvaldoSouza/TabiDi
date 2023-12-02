import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk

from .modal_adicionar import Modal_Adicionar
from .modal_alterar import Modal_Alterar

class Tela_EditCamp(tk.Toplevel): #TODO melhorar o nome da classe
    def __init__(self, classificacao_campeonato, db_path):
        super().__init__()
        self.geometry("900x600")
        self.resizable(width="TRUE", height="TRUE")
        self.title("Editor - Classificação do Campeonato")

        self.db_path = db_path

        # Cria a tabela
        self.construir_tabela_campeonatos(classificacao_campeonato)

        # Botão de adicionar
        self.adicionar_button = tk.Button(self, text="Adicionar", command=self.adicionar, bg="green", fg="black", font=("Arial", 14))
        self.adicionar_button.place(relx=0.9, rely=0.1, anchor="se")

        # Botão de alterar
        self.alterar_button = tk.Button(self, text="Alterar", command=self.alterar, bg="yellow", fg="black", font=("Arial", 14))
        self.alterar_button.place(relx=0.9, rely=0.2, anchor="se")

        # Botão de adicionar
        self.excluir_button = tk.Button(self, text="Excluir", command=self.excluir, bg="red", fg="black", font=("Arial", 14))
        self.excluir_button.place(relx=0.9, rely=0.3, anchor="se")

        # Botão de voltar
        self.voltar_button = tk.Button(self, text="Voltar", command=self.voltar, bg="blue", fg="black", font=("Arial", 14))
        self.voltar_button.place(relx=0.9, rely=0.4, anchor="se")

    def construir_tabela_campeonatos(self, classificacao_campeonato):
        colunas_campeonatos = ("Nome", "Pontos", "Vitórias", "Derrotas", "Empates")
        self.tabela_campeonatos = ttk.Treeview(self, columns=colunas_campeonatos, show='headings')

        for coluna in colunas_campeonatos:
            self.tabela_campeonatos.heading(coluna, text=coluna)
            self.tabela_campeonatos.column(coluna, width=100)  # Ajuste a largura conforme necessário

        for time in classificacao_campeonato:
            nome = time["nome"]
            #pontos = time["pontos"] sem pontos por enquanto
            vitorias = time["vitorias"]
            derrotas = time["derrotas"]
            empates = time["empates"]
            self.tabela_campeonatos.insert("", "end", values=(nome, vitorias, derrotas, empates))

        self.tabela_campeonatos.pack()

    def adicionar(self):
        modal_adicionar = Modal_Adicionar(self.db_path)  # Crie uma instância da classe Tela_User
        modal_adicionar.mainloop()
    
    def alterar(self):
        modal_alterar = Modal_Alterar()  # Crie uma instância da classe Tela_User
        modal_alterar.mainloop()
    
    def excluir(self):
        #TODO ligar ao banco
        pass
    
    def voltar(self):
        self.destroy()
