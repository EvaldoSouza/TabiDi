#Uma tela para mostrar os resultado da busca por usuários
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.messagebox import showinfo
from Controller import admin_controller

class AdminListarUsuarios(tk.Toplevel): 
    def __init__(self, root):
        super().__init__(root)
        self.db_path = "Database/db_usuarios.sqlite"


        self.controller = admin_controller.AdminController(self.db_path)
        #Geometria básica
        self.geometry("900x600")
        self.resizable(width="TRUE", height="TRUE")
        #barra de pesquisar usuário
        self.pesquisa_label = tk.Label(self, text="Pesquisar Usuário:", bg="#F0F0F0", font=("Arial", 12))
        self.usuario_pesquisado_var = tk.StringVar()
        self.entry_usuario_pesquisado = tk.Entry(self, font=("Arial", 14), textvariable=self.usuario_pesquisado_var)
        self.pesquisa_label.place(relx=0.1, rely=0.4, anchor="center")
        self.entry_usuario_pesquisado.place(relx=0.4, rely=0.4, anchor="center")

        self.entry_usuario_pesquisado.bind('<Return>', self.pesquisar)

         # Botões
        self.button1 = tk.Button(self, text="Voltar", command=self.voltar, bg="blue", fg="white", font=("Arial", 14))
        self.button1.place(relx=0.45, rely=0.6, anchor="center")

        #preciso mostrar uma tabela dinâmica
        #construindo a tabela
        self.lista_users = self.controller.consultar_todos_usuario()
        self.contruir_tabela(self.lista_users)
        
    def voltar(self):
        self.destroy()
    
    def exemplo_item_selecionado_evento(self, event):
        #fazendo igual ao exemplo por enquanto, para pegar a ideia
        for selected_item in self.tabela.selection(): #retorna um objeto tabela_entry
            item = self.tabela.item(selected_item) #retorna um dicionário com várias info
            record = item['values']
            showinfo(title='Informação', message=','.join(record))

    
    def tabela_selection(self):
        seletc_item = self.tabela.selection()[0]
        usuario = self.tabela.item(seletc_item, 'values')
        return usuario
            


    def usuario_selecionado_evento(self, event):
        #preciso abrir uma nova janela, dentro ou fora da main. Fora por enquanto
        #preciso que as informações mostradas nessa janela seja editavel pelo usuário
        #conferir se o usuário é ADM
        #salvar os dados editados
        
        record = self.tabela_selection()
            
        window = tk.Toplevel(self)
        window.geometry("500x300")
        

        user_label = tk.Label(window, text="Usuário: ", anchor="center")
        user_label.grid(row=0, column=0)
        user_info = tk.Label(window, text=record[0], anchor="center")
        user_info.grid(row=0, column=1)
        email_label = tk.Label(window, text="Email: ", anchor="center")
        email_label.grid(row=1, column=0)
        email_info = tk.Label(window, text=record[1], anchor="center")
        email_info.grid(row=1, column=1)

        privilege_label = tk.Label(window, text="Privilégio: ", anchor="center")
        privilege_label.grid(row=2, column=0)
        #privilege_var = tk.StringVar()
        privilege_info = tk.Label(window, text = record[2], anchor="center")
        privilege_info.grid(row=2, column=1)

        alterar_button = tk.Button(window, text="Incrementar Privilegio", command=lambda: self._alterar_privilegio(record[0], record[2]))
        alterar_button.grid(row=4, column=0)

        alterar_button = tk.Button(window, text="Reduzir Privilegio", command=lambda: self._reduzir_privilegio(record[0], record[2]))
        alterar_button.grid(row=4, column=1)

        deletar_buttor = tk.Button(window, text="Deletar Usuário", command=lambda: self._deletar_usuario(record[0]), bg="red", fg="white")
        deletar_buttor.grid(row=4, column=2)

        window.mainloop()

    def _alterar_privilegio(self, user_id, privilegio_atual):
        privilegio_atual = int(privilegio_atual)
        if privilegio_atual == 0:
            self.controller.update_privilegio(user_id, 1)
            print("Privilegio incrementado")
        if privilegio_atual == 1:
            self.controller.update_privilegio(user_id, 2)
            print("Privilegio incrementado")
    
    def _reduzir_privilegio(self, user_id, privilegio_atual):
        privilegio_atual = int(privilegio_atual)
        if privilegio_atual == 1:
            self.controller.update_privilegio(user_id, 0)
            print("Privilegio reduzido")
        if privilegio_atual == 2:
            self.controller.update_privilegio(user_id, 1)
            print("Privilegio reduzido")


    def _deletar_usuario(self, user_id):
        self.controller.deletar_usuario(user_id)
        print("usuario deletado")
        
    def inserir_item(self,tabela, item):
        #está apenas inserindo, não checa se é um usuário válido
        #seria bom se tratasse dos casos de uso corrompidos e talz
        tabela.insert('', 'end', text='1', values=item)
    
    def main_display_users(self):
        #preciso ler do banco de dados e mostrar aqui
        self.title("TaBedi")
        self.update()
    
    def pesquisar(self, event):
        parametro = self.entry_usuario_pesquisado.get()
        print(parametro)
        resultado = self.controller.pesquisar_usuario(parametro)
        self.contruir_tabela(resultado)

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
            self.inserir_item(self.tabela, user)
        
        self.tabela.bind('<<TreeviewSelect>>', self.usuario_selecionado_evento)
        #self.tabela.bind("<ButtonPress>", self.exemplo_item_selecionado_evento)
        
        self.tabela.pack()

    def mostrar_categorias_usuarios(self, enum_categorias):
        window = tk.Toplevel(self)
        window.title("Categorias de Usuário")

        
        radiobuttons = []
        for categoria in enum_categorias:
            radiobutton = tk.Radiobutton(window, text=f"Privilegio de {categoria}", value=categoria)
            radiobutton.pack()
            radiobuttons.append(radiobutton)
            
        selected_option = tk.StringVar(window)

        for radiobutton in radiobuttons:
            radiobutton.config(variable=selected_option)

        select_button = tk.Button(window, text="Selecionar", command=lambda: self._close_return_button(window, selected_option))
        select_button.pack()
    
    def _close_return_button(self, window, value):
        #print("valor selecionado: ", value.get())
        self.controller.recebe_valor_de_janela(value.get())
        window.destroy()
        return value.get()
    