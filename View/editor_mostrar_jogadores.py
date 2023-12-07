#Uma tela para mostrar os resultado da busca por usuários
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.messagebox import showinfo
from Controller import editor_controller
from .editor_criar_jogador import EditorCriarNovoJogador

class EditorMostrarJogadores(tk.Toplevel): 
    def __init__(self, db_path, root, time, complemento):
        super().__init__(root)
        self.db_path = db_path
        self.time = time
        self.complemento = complemento


        self.controller = editor_controller.EditorController(self.db_path)
        #Geometria básica
        self.geometry("900x600")
        self.resizable(width="TRUE", height="TRUE")

                        # Adicionando um logotipo
        self.logo_image = PhotoImage(file="View/img/logo.png")
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.place(relx=0.5, rely=0.15, anchor="center")
        
        #barra de pesquisar usuário
        self.pesquisa_label = tk.Label(self, text="Pesquisar Jogador:", bg="#F0F0F0", font=("Arial", 12))
        self.usuario_pesquisado_var = tk.StringVar()
        self.entry_usuario_pesquisado = tk.Entry(self, font=("Arial", 14), textvariable=self.usuario_pesquisado_var)
        self.pesquisa_label.place(relx=0.1, rely=0.4, anchor="center")
        self.entry_usuario_pesquisado.place(relx=0.4, rely=0.4, anchor="center")

        self.entry_usuario_pesquisado.bind('<Return>', self.pesquisar)

         # Botões
        self.button1 = tk.Button(self, text="Adicionar Jogador", command=self.adicionar_jogador, bg="green", fg="black", font=("Arial", 14))
        self.button1.place(relx=0.45, rely=0.5, anchor="center")
        self.button1 = tk.Button(self, text="Deletar Jogador", command=self.deletar_jogador, bg="red", fg="black", font=("Arial", 14))
        self.button1.place(relx=0.45, rely=0.7, anchor="center")


        self.button1 = tk.Button(self, text="Atualizar", command=self.atualizar, bg="green", fg="black", font=("Arial", 14))
        self.button1.place(relx=0.1, rely=0.5, anchor="center")
        self.button1 = tk.Button(self, text="Voltar", command=self.voltar, bg="blue", fg="white", font=("Arial", 14))
        self.button1.place(relx=0.1, rely=0.6, anchor="center")

        #preciso mostrar uma tabela dinâmica
        #construindo a tabela
        # self.lista_users = self.controller.todos_jogadores_do_time(self.time, self.complemento)
        # self.construir_tabela(self.lista_users)
        self.atualizar()

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
    
        
    def inserir_item(self,tabela, item):
        #está apenas inserindo, não checa se é um usuário válido
        #seria bom se tratasse dos casos de uso corrompidos e talz
        tabela.insert('', 'end', text='1', values=item)
    
    
    def pesquisar(self, event):
        parametro = self.entry_usuario_pesquisado.get()
        resultado = self.controller.pesquisar_qualquer(parametro)
        self.construir_tabela(resultado)

    def construir_tabela(self, lista_users):
        try:
            self.tabela.destroy()
        except AttributeError:
            #print("Criando nova tabela?")
            pass
        
        self.colunas = ("nome", "apelido", "posição")
        self.tabela = ttk.Treeview(self, columns=self.colunas, show='headings')
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("apelido", text="Apelido")
        self.tabela.heading("posição", text="Posição")
        #TODO fazer que seja uma tabela com scroll --Evaldo

        for user in lista_users:
            self.inserir_item(self.tabela, user)
        
        self.tabela.bind('<<TreeviewSelect>>', self.jogador_selecionado)
        #self.tabela.bind("<ButtonPress>", self.exemplo_item_selecionado_evento)
        
        self.tabela.pack()

    def jogador_selecionado(self, event):
        jogador_selecionado = self.tabela.selection()
        if jogador_selecionado:
            self.jogador_dados = self.tabela.item(jogador_selecionado)["values"]
        
    
    def _close_return_button(self, window, value):
        #print("valor selecionado: ", value.get())
        self.controller.recebe_valor_de_janela(value.get())
        window.destroy()
        return value.get()
    
    def adicionar_jogador(self):
        novo_jogador = EditorCriarNovoJogador(self.time, self.complemento, self.db_path)
        novo_jogador.mainloop()
    
    def deletar_jogador(self):
        if self.jogador_dados:
            if self.controller.excluir_jogador(self.jogador_dados[0], self.jogador_dados[1]):
                print("Jogador excluido:", self.jogador_dados[0])
        

    def editar_jogador(self):
        pass
    
    def atualizar(self):
        self.lista_users = self.controller.todos_jogadores_do_time(self.time, self.complemento)
        self.construir_tabela(self.lista_users)