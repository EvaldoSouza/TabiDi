import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import os

from .editor_editar_camp import EditorEditarCamp
from .editor_criar_campeonato import EditorCriarCampeonato
from Controller import leitor_controller, editor_controller

class EditorListarCamps(tk.Toplevel):
    def __init__(self, root, controller, lista_campeonatos):
        super().__init__(root)

        self.root = root

        #para trabalhar com o campeonato selecionado
        self.selected_campeonato = None  # Variable to store the selected campeonato

        self.controller = controller
        self.geometry("900x600")
        self.resizable(width="TRUE", height="TRUE")
        self.title("Editor - Lista de Campeonatos")

        self.background_image = PhotoImage(file="View/img/football_background.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Lista de campeonatos
        self.construir_lista_campeonatos(lista_campeonatos)

        self.cadastrar_button = tk.Button(self, text="Cadastrar Campeonato", command=self.cadastrar_campeonato, bg="black", fg="white", font=("Arial", 14))
        self.cadastrar_button.place(relx=0.1, rely=0.6, anchor="w")

        self.selecionar_button = tk.Button(self, text="Selecionar", command=self.selecionar, bg="green", fg="white", font=("Arial", 14))
        self.selecionar_button.place(relx=0.9, rely=0.2, anchor="se")

        self.selecionar_button = tk.Button(self, text="Deletar", command=self.deletar, bg="red", fg="white", font=("Arial", 14))
        self.selecionar_button.place(relx=0.9, rely=0.3, anchor="se")

        self.voltar_button = tk.Button(self, text="Voltar", command=self.voltar, bg="yellow", fg="black", font=("Arial", 14))
        self.voltar_button.place(relx=0.9, rely=0.4, anchor="se")

        self.atualizar_button = tk.Button(self, text="Atualizar", command=self.atualizar, bg="green", fg="white", font=("Arial", 14))
        self.atualizar_button.place(relx=0.1, rely=0.7, anchor="w")

    def cadastrar_campeonato(self):
        tela_editor_novocamp = EditorCriarCampeonato()
        tela_editor_novocamp.mainloop()
        #Não consegui atualizar a tabela nessa função
        

    def atualizar(self):
        self.lista_campeonatos_listbox.delete(0, tk.END)
        db_path = "Database/lista_campeonatos.sqlite"
        editor = editor_controller.EditorController(db_path)
        lista_campeonatos = editor.recuperar_campeonatos()
        self.construir_lista_campeonatos(lista_campeonatos)

    def voltar(self):
        self.destroy()
    
    def construir_lista_campeonatos(self, lista_campeonatos):
        if not lista_campeonatos:
            print("Lista vazia")
            return
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

    def deletar(self):
        if self.selected_campeonato:
            name = self.selected_campeonato.split(":")[0].strip()
            print(f"Deletado campeonato: {name} --tela_editor_pesquisar")
            db_path = "Database/lista_campeonatos.sqlite"
            editor = editor_controller.EditorController(db_path)
            editor.excluir_campeonato(name)
            self.atualizar()

    def selecionar(self):
        # Chame construir_tabela_campeonatos para criar a tabela antes de acessá-la
        
        #seguindo a ideia de que o editor vai criar um campeonato,e que o nome dele sera o msm do arquivo
        if self.selected_campeonato:
            name = self.selected_campeonato.split(":")[0].strip()
            campeonato_db = "Database/Campeonatos/"+ name +".sqlite"
            if os.path.exists(campeonato_db):
                tela_campeonato = EditorEditarCamp(self.root, campeonato_db)
                #TODO destruir essa janela aqui quando tiver funcionando
                tela_campeonato.mainloop()
            else:
                #TODO Tratar esse erro propriamente
                print("Campeonato não existe em tela_editor_pesquisar")

