#Uma tela para mostrar os resultado da busca por usuários
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.messagebox import showinfo

class Display_Users(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        #Geometria básica
        self.geometry("900x600")
        self.resizable(width="TRUE", height="TRUE")
         # Adicionando uma imagem de fundo
        self.background_image = PhotoImage(file="View/football_background.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        #preciso mostrar uma tabela dinâmica
        #construindo a tabela
        self.colunas = ("usuario", "email", "privilegio")
        self.tabela = ttk.Treeview(self, columns=self.colunas, show='headings')
        self.tabela.heading("usuario", text="Usuário")
        self.tabela.heading("email", text="Email")
        self.tabela.heading("privilegio", text="Privilégio")

        #preciso realizar consultas ao banco de dados, o que é feito no controller

    def item_selecionado_evento(self):
        #fazendo igual ao exemplo por enquanto, para pegar a ideia
        for selected_item in self.tabela.selection():
            item = self.tabela(selected_item)
            record = item['values']
            showinfo(title='Informação', message=','.join(record))
    
    


