import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from .tela_camp import Tela_Classificacao

lista_campeonatos = [
    #TODO Puxar do banco de dados
    {"nome": "Campeonato 1", "descricao": "Descrição do Campeonato 1"},
    {"nome": "Campeonato 2", "descricao": "Descrição do Campeonato 2"},
]
classificacao = [
    {"nome": "Time A", "pontos": 12, "vitorias": 4, "derrotas": 2, "empates": 0},
    {"nome": "Time B", "pontos": 10, "vitorias": 3, "derrotas": 1, "empates": 1},
    {"nome": "Time C", "pontos": 8, "vitorias": 2, "derrotas": 2, "empates": 2},
    {"nome": "Time D", "pontos": 6, "vitorias": 1, "derrotas": 3, "empates": 3},
    {"nome": "Time E", "pontos": 4, "vitorias": 0, "derrotas": 4, "empates": 4},
]
class Tela_Campeonatos(tk.Toplevel):
    def __init__(self, controller, lista_campeonatos):
        super().__init__()
        self.controller = controller
        self.geometry("900x600")
        self.resizable(width="TRUE", height="TRUE")
        self.title("Lista de Campeonatos")

        self.background_image = PhotoImage(file="View/img/football_background.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Lista de campeonatos
        self.construir_lista_campeonatos(lista_campeonatos)

        self.selecionar_button = tk.Button(self, text="Selecionar", command=self.ranking, bg="green", fg="white", font=("Arial", 14))
        self.selecionar_button.place(relx=0.9, rely=0.2, anchor="se")

        self.voltar_button = tk.Button(self, text="Voltar", command=self.voltar, bg="yellow", fg="black", font=("Arial", 14))
        self.voltar_button.place(relx=0.9, rely=0.3, anchor="se")

    def construir_lista_campeonatos(self, lista_campeonatos):
        # Implemente a construção da lista de campeonatos aqui, com base em 'lista_campeonatos'
        # Use Treeview ou outra estrutura adequada

        pass

    def ranking(self):
        tela_classificacao = Tela_Classificacao(self.controller)
        tela_classificacao.mainloop()

    def voltar(self):
        self.destroy()
        pass
    
    def construir_lista_campeonatos(self, lista_campeonatos):
        lista_frame = tk.Frame(self)
        lista_frame.place(relx=0.1, rely=0.3, anchor="w")

        lista_scrollbar = tk.Scrollbar(lista_frame, orient="vertical")
        lista_scrollbar.pack(side="right", fill="y")

        lista_campeonatos_listbox = tk.Listbox(lista_frame, yscrollcommand=lista_scrollbar.set, width=40, height=10, font=("Arial", 14))
        lista_campeonatos_listbox.pack(side="left", fill="both", expand=True)

        for campeonato in lista_campeonatos:
            nome = campeonato["nome"]
            descricao = campeonato["descricao"]
            lista_campeonatos_listbox.insert("end", f"{nome}: {descricao}")

        lista_scrollbar.config(command=lista_campeonatos_listbox.yview)


    def construir_tabela_campeonatos(self, lista_campeonatos):
        try:
            self.tabela_campeonatos.destroy()
        except AttributeError:
            print("Criando nova tabela de campeonatos?")

        colunas_campeonatos = ("nome", "descricao")
        self.tabela_campeonatos = ttk.Treeview(self, columns=colunas_campeonatos, show='headings')
        self.tabela_campeonatos.heading("nome", text="Nome")
        self.tabela_campeonatos.heading("descricao", text="Descrição")

        for campeonato in lista_campeonatos:
            self.inserir_item(self.tabela_campeonatos, campeonato)

        self.tabela_campeonatos.pack()

    def inserir_item_campeonatos(self, tabela, campeonato):
        tabela.insert('', 'end', values=(campeonato["nome"], campeonato["descricao"]))
        

    def tabela_selection_campeonato(self):
        selected_item = self.tabela_campeonatos.selection()[0]
        campeonato = self.tabela_campeonatos.item(selected_item, 'values')
        return campeonato

    def selecionar_campeonato_evento(self):
        # Implemente a lógica para selecionar um campeonato
        record = self.tabela_selection_campeonato()
        print(f"Campeonato selecionado: Nome - {record[0]}, Descrição - {record[1]}")

    def ranking(self):
        tela_classificacao = Tela_Classificacao(self.controller,classificacao)
        tela_classificacao.mainloop()
        
        