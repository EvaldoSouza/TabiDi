import tkinter as tk
from tkinter import ttk

class LeitorListarTimes(tk.Toplevel): #TODO melhorar o nome da classe
    def __init__(self, classificacao_campeonato):
        super().__init__()
        self.geometry("900x600")
        self.resizable(width="TRUE", height="TRUE")
        self.title("Leitor - Classificação do Campeonato")

        # Cria a tabela
        self.construir_tabela_campeonatos(classificacao_campeonato)

        # Botão de voltar
        self.voltar_button = tk.Button(self, text="Voltar", command=self.voltar, bg="yellow", fg="black", font=("Arial", 14))
        self.voltar_button.place(relx=0.9, rely=0.1, anchor="se")

    def construir_tabela_campeonatos(self, classificacao_campeonato):
        colunas_campeonatos = ("Nome", "Pontos", "Vitórias", "Derrotas", "Empates")
        self.tabela_campeonatos = ttk.Treeview(self, columns=colunas_campeonatos, show='headings')

        for coluna in colunas_campeonatos:
            self.tabela_campeonatos.heading(coluna, text=coluna)
            self.tabela_campeonatos.column(coluna, width=100)  # Ajuste a largura conforme necessário

        for time in classificacao_campeonato:
            nome = time["nome"]
            pontos = time["pontos"]
            vitorias = time["vitorias"]
            derrotas = time["derrotas"]
            empates = time["empates"]
            self.tabela_campeonatos.insert("", "end", values=(nome, pontos, vitorias, derrotas, empates))

        self.tabela_campeonatos.pack()

    def voltar(self):
        self.destroy()
