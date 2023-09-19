#Uma tela para mostrar os resultado da busca por usuários
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.messagebox import showinfo

#TODO criar uma classe  Dislpay_Table e fazer herança, para padronizar a visualização
class Display_Users(tk.Tk):
    def __init__(self, controller, lista_users):
        super().__init__()
        self.controller = controller
        #Geometria básica
        self.geometry("900x600")
        self.resizable(width="TRUE", height="TRUE")
         # Adicionando uma imagem de fundo...como fazer isso? Se colocar self, da erro
        #self.background_image = PhotoImage(file="View/football_background.png")
        #self.background_label = tk.Label(tk.Toplevel(), image=self.background_image)
        #self.background_label.place(relwidth=1, relheight=1)

        #preciso mostrar uma tabela dinâmica
        #construindo a tabela
        self.colunas = ("usuario", "email", "privilegio")
        self.tabela = ttk.Treeview(self, columns=self.colunas, show='headings')
        self.tabela.heading("usuario", text="Usuário")
        self.tabela.heading("email", text="Email")
        self.tabela.heading("privilegio", text="Privilégio")

        for user in lista_users:
            self.inserir_item(user)
        
        self.tabela.bind("<ButtonPress>", self.exemplo_item_selecionado_evento)
        self.tabela.pack()

    def exemplo_item_selecionado_evento(self, event):
        #fazendo igual ao exemplo por enquanto, para pegar a ideia
        for selected_item in self.tabela.selection():
            item = self.tabela.item(selected_item)
            record = item['values']
            showinfo(title='Informação', message=','.join(record))

    def inserir_item(self, item):
        #está apenas inserindo, não checa se é um usuário válido
        #seria bom se tratasse dos casos de uso corrompidos e talz
        self.tabela.insert('', 'end', text='1', values=item)
    
    def main_display_users(self):
        #preciso ler do banco de dados e mostrar aqui
        self.title("TaBedi")
        self.mainloop()
    