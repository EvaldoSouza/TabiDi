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
         #TODO Adicionando uma imagem de fundo...como fazer isso? Se colocar self, da erro --Evaldo
        #self.background_image = PhotoImage(file="View/football_background.png")
        #self.background_label = tk.Label(tk.Toplevel(), image=self.background_image)
        #self.background_label.place(relwidth=1, relheight=1)

        #barra de pesquisar usuário
        self.pesquisa_label = tk.Label(self, text="Pesquisar Usuário:", bg="#F0F0F0", font=("Arial", 12))
        self.usuario_pesquisado_var = tk.StringVar()
        self.entry_usuario_pesquisado = tk.Entry(self, font=("Arial", 14), textvariable=self.usuario_pesquisado_var)
        self.pesquisa_label.place(relx=0.1, rely=0.4, anchor="center")
        self.entry_usuario_pesquisado.place(relx=0.4, rely=0.4, anchor="center")

        self.entry_usuario_pesquisado.bind('<Return>', self.pesquisar)


        #preciso mostrar uma tabela dinâmica
        #construindo a tabela
        self.contruir_tabela(lista_users)
        
        
        self.tabela.bind("<ButtonPress>", self.exemplo_item_selecionado_evento)
        

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
        self.update()
    
    def pesquisar(self, event):
        print("Enter GUI\n")
        parametro = self.entry_usuario_pesquisado.get()
        self.controller.adm_pesquisa_usuario(parametro)

    def contruir_tabela(self, lista_users):
        try:
            self.tabela.destroy()
        except AttributeError:
            print("Criando nova tabela?")
        
        self.colunas = ("usuario", "email", "privilegio")
        self.tabela = ttk.Treeview(self, columns=self.colunas, show='headings')
        self.tabela.heading("usuario", text="Usuário")
        self.tabela.heading("email", text="Email")
        self.tabela.heading("privilegio", text="Privilégio")
        #TODO fazer que seja uma tabela com scroll --Evaldo

        for user in lista_users:
            self.inserir_item(user)
        
        self.tabela.pack()