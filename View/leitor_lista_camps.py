import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import os

from View import leitor_listar_times
#from .tela_editor_novo_camp import TelaEditorNovoCamp
from Controller import leitor_controller



class LeitorListaCamps(tk.Toplevel):
    def __init__(self, controller, lista_campeonatos):
        super().__init__()
        #para trabalhar com o campeonato selecionado
        self.selected_campeonato = None  # Variable to store the selected campeonato

        self.controller = controller
        self.geometry("900x600")
        self.resizable(width="TRUE", height="TRUE")
        #self.title("Editor - Lista de Campeonatos")
        self.title("Leitor - Lista de Campeonatos")
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

        self.lista_campeonatos_listbox = tk.Listbox(lista_frame, yscrollcommand=lista_scrollbar.set, width=40, height=10, font=("Arial", 14))
        self.lista_campeonatos_listbox.pack(side="left", fill="both", expand=True)

        for campeonato in lista_campeonatos:
            nome = campeonato[0]
            ano = campeonato[1]
            self.lista_campeonatos_listbox.insert("end", f"{nome}: {ano}")

        lista_scrollbar.config(command=self.lista_campeonatos_listbox.yview)
        self.lista_campeonatos_listbox.bind("<<ListboxSelect>>", self.on_listbox_select)

    def on_listbox_select(self, event):
        # Get the selected item from the listbox
        selected_index = self.lista_campeonatos_listbox.curselection()
        if selected_index:
            self.selected_campeonato = self.lista_campeonatos_listbox.get(selected_index)



    def construir_tabela_campeonatos(self, classificacao_campeonato):
        try:
            self.tabela_campeonatos.destroy()
        except AttributeError:
            print("Criando nova tabela de campeonatos? --tela_lista_camps")
            

        #colunas_campeonatos = ("nome", "pontos", "vitorias", "derrotas", "empates") sem os pontos por enquanto
        colunas_campeonatos = ("nome", "vitorias", "derrotas", "empates")
        self.tabela_campeonatos = ttk.Treeview(self, columns=colunas_campeonatos, show='headings')
        
        for coluna in colunas_campeonatos:
            self.tabela_campeonatos.heading(coluna, text=coluna.capitalize())  # Use o nome da coluna como título

        for time in classificacao_campeonato:
            self.tabela_campeonatos.insert('', 'end', values=(time["nome"],  time["vitorias"], time["derrotas"], time["empates"]))

        tela_leitor_camp = leitor_listar_times.LeitorListarTimes(classificacao_campeonato)
        tela_leitor_camp.mainloop()



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
        
        #seguindo a ideia de que o editor vai criar um campeonato,e que o nome dele sera o msm do arquivo
        if self.selected_campeonato:
            name = self.selected_campeonato.split(":")[0].strip()
            print(f"Selected campeonato: {name} --tela_editor_pesquisar")
            campeonato_db = "Database/Campeonatos/"+ name +".sqlite"
            if os.path.exists(campeonato_db):
                #self.leitor.set_db_path(campeonato_db)
                #times= self.leitor.retorna_times()
                leitor = leitor_controller.LeitorController(campeonato_db)
                times = leitor.listar_times()
                self.construir_tabela_campeonatos(times)
                self.tabela_selection_campeonato()
            else:
                #TODO Tratar esse erro propriamente
                print("Campeonato não existe em tela_editor_leitor")

