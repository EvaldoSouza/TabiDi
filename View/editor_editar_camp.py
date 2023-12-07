import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import os
from .editor_mostrar_jogadores_campeonato import EditorMostrarJogadoresCampeonato
from .editor_criar_novo_time import EditorCriarNovoTime
from .editor_alterar_time import EditorAlterarTime
from .editor_criar_jogador import EditorCriarNovoJogador
from .editor_mostrar_jogadores import EditorMostrarJogadores
from .editor_cadastrar_partida import EditorCadastrarPartida
from .editor_mostrar_partidas import EditorMostrarPartidas
from Controller import editor_controller

class EditorEditarCamp(tk.Toplevel): #TODO melhorar o nome da classe
    def __init__(self, root, db_path):
        super().__init__(root)
        self.geometry("900x600")
        self.resizable(width="TRUE", height="TRUE")
        self.title("Editor - Editar Campeonato")

                # Adicionando um logotipo
        self.logo_image = PhotoImage(file="View/img/logo.png")
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.place(relx=0.5, rely=0.15, anchor="center")

        self.db_path = db_path

        self.controller = editor_controller.EditorController(self.db_path)

        # Cria a tabela
        self.construir_tabela_times(self.times())

        # Botão de adicionar
        self.adicionar_button = tk.Button(self, text="Adicionar Time", command=self.adicionar, bg="green", fg="black", font=("Arial", 14))
        self.adicionar_button.place(relx=0.9, rely=0.1, anchor="se")

        # Botão de alterar
        self.alterar_button = tk.Button(self, text="Alterar Time", command=self.alterar, bg="yellow", fg="black", font=("Arial", 14))
        self.alterar_button.place(relx=0.9, rely=0.2, anchor="se")

        # Botão de adicionar
        self.excluir_button = tk.Button(self, text="Excluir Time", command=self.excluir, bg="red", fg="black", font=("Arial", 14))
        self.excluir_button.place(relx=0.9, rely=0.3, anchor="se")

        # Botão de voltar
        self.voltar_button = tk.Button(self, text="Voltar", command=self.voltar, bg="blue", fg="black", font=("Arial", 14))
        self.voltar_button.place(relx=0.9, rely=0.4, anchor="se")

        #botao de atualizar 
        self.atualizar_button = tk.Button(self, text="Atualizar", command=self.atualizar, bg="green", fg="white", font=("Arial", 14))
        self.atualizar_button.place(relx=0.9, rely=0.4, anchor="se")

        self.atualizar_button = tk.Button(self, text="Cadastrar Partida", command=self.cadastrar_partida, bg="yellow", fg="black", font=("Arial", 14))
        self.atualizar_button.place(relx=0.9, rely=0.6, anchor="se")

        self.atualizar_button = tk.Button(self, text="Motrar Partidas", command=self.mostrar_partidas, bg="green", fg="black", font=("Arial", 14))
        self.atualizar_button.place(relx=0.9, rely=0.5, anchor="se")

        self.atualizar_button = tk.Button(self, text="Mostrar Jogadores", command=self.mostrar_jogadores, bg="blue", fg="white", font=("Arial", 14))
        self.atualizar_button.place(relx=0.9, rely=0.7, anchor="se")

        self.mostrar_jogadores_campeonato_button = tk.Button(self, text="Mostrar Jogadores Campeonato", command=self.mostrar_jogadores_campeonato, bg="blue", fg="white", font=("Arial", 14))
        self.mostrar_jogadores_campeonato_button.place(relx=0.9, rely=0.8, anchor="se")



    def construir_tabela_times(self, classificacao_campeonato):
        try:
            self.tabela_times.destroy()
        except AttributeError:
            print("Criando nova tabela de campeonatos?")
            #print(classificacao_campeonato)
        
        colunas_times = ("Nome", "Complemento" "Pontos", "Vitórias", "Derrotas", "Empates")
        self.tabela_times = ttk.Treeview(self, columns=colunas_times, show='headings')

        for coluna in colunas_times:
            self.tabela_times.heading(coluna, text=coluna.capitalize())
            self.tabela_times.column(coluna, width=70)  # Ajuste a largura conforme necessário

        if classificacao_campeonato:
            for time in classificacao_campeonato:
                nome = time["nome"]
                complemento = time["complemento"]
                pontos = time["pontos"]
                vitorias = time["vitorias"]
                derrotas = time["derrotas"]
                empates = time["empates"]
                self.tabela_times.insert("", "end", values=(nome, complemento, pontos, vitorias, derrotas, empates))

        self.tabela_times.pack()
        self.tabela_times.bind("<<TreeviewSelect>>", self.on_treeviw_select )

    def on_treeviw_select(self, event):
        time_selecionado = self.tabela_times.selection() #retorna apenas o nome do time (primeiro elemento). Tem que usar .item para pegar os valores
        if time_selecionado:
            #self.time_selecionado = time_selecionado[0] #por algum motivo ta tundo vindo no values
            self.dados_time_selecionado = self.tabela_times.item(time_selecionado)["values"] #os dados do time
            self.time_selecionado = self.dados_time_selecionado[0]

    def adicionar(self):
        modal_adicionar = EditorCriarNovoTime(self.db_path)  # Crie uma instância da classe Tela_User
        modal_adicionar.mainloop()
    
    #TODO Fazer isso funcionar
    def alterar(self):
        modal_alterar = EditorAlterarTime(self.db_path)  # Crie uma instância da classe Tela_User
        modal_alterar.mainloop()
        #mandar os dados atuais?
    
    def excluir(self):
        if self.controller.excluir_time(self.time_selecionado, self.dados_time_selecionado[1]):
            print("Time {} com complemento {} foi exlcluido corretamente", self.time_selecionado, self.dados_time_selecionado[0])

        else:
            print("Time {} com complemento {} não foi exlcluido corretamente", self.time_selecionado, self.dados_time_selecionado[0])

        pass

    def atualizar(self):
        self.tabela_times.delete(*self.tabela_times.get_children())
        self.construir_tabela_times(self.times())
        
    
    def voltar(self):
        self.destroy()

    def times(self):
        return self.controller.recuperar_times()
    
    def mostrar_jogadores(self):
        if self.time_selecionado:
            jogadores = EditorMostrarJogadores(self.db_path, self, self.dados_time_selecionado[0], self.dados_time_selecionado[1])
            jogadores.mainloop()

    def cadastrar_partida(self):
        partida = EditorCadastrarPartida(self, self.db_path)
        partida.mainloop()
        
    def mostrar_partidas(self):
        mostrar_partidas = EditorMostrarPartidas(self, self.db_path)
        mostrar_partidas.mainloop()

    def mostrar_jogadores_campeonato(self):
      # Chame construir_tabela_campeonatos para criar a tabela antes de acessá-la
      
      #seguindo a ideia de que o editor vai criar um campeonato,e que o nome dele sera o msm do arquivo
      if os.path.exists(self.db_path):
          tela_jogador_campeonato = EditorMostrarJogadoresCampeonato(self.db_path, self)
          #TODO destruir essa janela aqui quando tiver funcionando
          tela_jogador_campeonato.mainloop()
      else:
          #TODO Tratar esse erro propriamente
          print("Campeonato não existe em tela_editor_pesquisar")