import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import ttk

class Tela_Classificacao(tk.Toplevel):
    def __init__(self, controller, classificacao):
        super().__init__(controller)
        self.controller = controller
        self.geometry("900x600")
        self.resizable(width="TRUE", height="TRUE")
        self.title("Classificação do Campeonato")

        # Barra de pesquisa
        self.pesquisa_label = tk.Label(self, text="Pesquisar Time:", bg="#F0F0F0", font=("Arial", 12))
        self.time_pesquisado_var = tk.StringVar()
        self.entry_time_pesquisado = tk.Entry(self, font=("Arial", 14), textvariable=self.time_pesquisado_var)
        self.pesquisa_label.place(relx=0.1, rely=0.1, anchor="w")
        self.entry_time_pesquisado.place(relx=0.3, rely=0.1, anchor="w")

        self.entry_time_pesquisado.bind('<Return>', self.pesquisar_time)

        # Tabela de Classificação
        colunas = ("Nome", "Pontos", "Vitórias", "Derrotas", "Empates")
        self.tabela_classificacao = ttk.Treeview(self, columns=colunas, show="headings")
        for coluna in colunas:
            self.tabela_classificacao.heading(coluna, text=coluna)
            self.tabela_classificacao.column(coluna, width=100)  # Ajuste a largura conforme necessário

        self.construir_classificacao(classificacao)

        self.tabela_classificacao.bind('<<TreeviewSelect>>', self.time_selecionado_evento)

        # Botões
        self.pesquisar_button = tk.Button(self, text="Pesquisar", command=self.pesquisar_time, bg="blue", fg="white", font=("Arial", 14))
        self.pesquisar_button.place(relx=0.9, rely=0.1, anchor="se")

        self.voltar_button = tk.Button(self, text="Voltar", command=self.voltar, bg="yellow", fg="black", font=("Arial", 14))
        self.voltar_button.place(relx=0.9, rely=0.3, anchor="se")

    def construir_classificacao(self, classificacao):
        for time in classificacao:
            nome = time["nome"]
            pontos = time["pontos"]
            vitorias = time["vitorias"]
            derrotas = time["derrotas"]
            empates = time["empates"]
            self.tabela_classificacao.insert("", "end", values=(nome, pontos, vitorias, derrotas, empates))

    def pesquisar_time(self, event):
        parametro = self.time_pesquisado_var.get()
        # Implemente a lógica para pesquisar um time na classificação do campeonato
        pass

    def time_selecionado_evento(self, event):
        # Implemente a lógica para lidar com a seleção de um time na classificação
        pass

    def voltar(self):
        self.destroy()
