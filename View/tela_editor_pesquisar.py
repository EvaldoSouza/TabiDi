import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

from View.tela_editcamp import Tela_EditCamp

lista_campeonatos = [
    #TODO Puxar do banco de dados
    {"nome": "Campeonato 1", "descricao": "Descrição do Campeonato 1"},
    {"nome": "Campeonato 2", "descricao": "Descrição do Campeonato 2"},
]
classificacao_campeonato = [
    #TODO Puxar do banco de dados
    {"nome": "Time A", "pontos": 12, "vitorias": 4, "derrotas": 2, "empates": 0},
    {"nome": "Time B", "pontos": 10, "vitorias": 3, "derrotas": 1, "empates": 1},
    {"nome": "Time C", "pontos": 8, "vitorias": 2, "derrotas": 2, "empates": 2},
    {"nome": "Time D", "pontos": 6, "vitorias": 1, "derrotas": 3, "empates": 3},
    {"nome": "Time E", "pontos": 4, "vitorias": 0, "derrotas": 4, "empates": 4},
]

class Tela_Editor_Pesquisar(tk.Toplevel):
    def __init__(self, controller, lista_campeonatos):
        super().__init__()
        self.controller = controller
        self.geometry("900x600")
        self.resizable(width="TRUE", height="TRUE")
        self.title("Editor - Lista de Campeonatos")

        self.tabela_campeonatos = None

        self.background_image = PhotoImage(file="View/img/football_background.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Lista de campeonatos
        self.construir_lista_campeonatos(lista_campeonatos)

        self.selecionar_button = tk.Button(self, text="Selecionar", command=self.ranking, bg="green", fg="white", font=("Arial", 14))
        self.selecionar_button.place(relx=0.9, rely=0.2, anchor="se")

        self.voltar_button = tk.Button(self, text="Voltar", command=self.voltar, bg="yellow", fg="black", font=("Arial", 14))
        self.voltar_button.place(relx=0.9, rely=0.3, anchor="se")


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


    def construir_tabela_campeonatos(self, classificacao_campeonato):
        try:
            self.tabela_campeonatos.destroy()
        except AttributeError:
            print("Criando nova tabela de campeonatos?")

        colunas_campeonatos = ("nome", "pontos", "vitorias", "derrotas", "empates")
        self.tabela_campeonatos = ttk.Treeview(self, columns=colunas_campeonatos, show='headings')
        
        for coluna in colunas_campeonatos:
            self.tabela_campeonatos.heading(coluna, text=coluna.capitalize())  # Use o nome da coluna como título

        for time in classificacao_campeonato:
            self.tabela_campeonatos.insert('', 'end', values=(time["nome"], time["pontos"], time["vitorias"], time["derrotas"], time["empates"]))

        tela_editorcamp = Tela_EditCamp(classificacao_campeonato)
        tela_editorcamp.mainloop()



    def inserir_item_campeonatos(self, tabela, campeonato):
        tabela.insert('', 'end', values=(campeonato["nome"], campeonato["descricao"]))
        

    def tabela_selection_campeonato(self):
        selected_item = self.tabela_campeonatos.selection()
        campeonato = self.tabela_campeonatos.item(selected_item, 'values')
        return campeonato

    def selecionar_campeonato_evento(self):
        # Implemente a lógica para selecionar um campeonato
        record = self.tabela_selection_campeonato()
        print(f"Campeonato selecionado: Nome - {record[0]}, Descrição - {record[1]}")

    def ranking(self):
        # Chame construir_tabela_campeonatos para criar a tabela antes de acessá-la
        self.construir_tabela_campeonatos(classificacao_campeonato)
        campeonato_selecionado = self.tabela_selection_campeonato()
        if campeonato_selecionado:
            tela_editorcamp = Tela_EditCamp(self.controller, classificacao_campeonato)
            tela_editorcamp.mainloop()
