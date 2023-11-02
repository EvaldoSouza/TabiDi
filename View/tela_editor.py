import tkinter as tk
from tkinter import PhotoImage
from .tela_editor_pesquisar import Tela_Editor_Pesquisar

lista_campeonatos = [
    {"nome": "Campeonato 1", "descricao": "Descrição do Campeonato 1"},
    {"nome": "Campeonato 2", "descricao": "Descrição do Campeonato 2"},
    # Adicione mais campeonatos, se necessário
]
class Tela_Editor(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        # Geometria básica
        self.title('Home - Editor')
        self.geometry("900x600")
        self.resizable(width=False, height=False)
        # Adicionando uma imagem de fundo
        self.background_image = PhotoImage(file="View/img/football_background.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Adicionando uma logo
        self.logo_image = PhotoImage(file="View/img/logo.png")
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.place(relx=0.5, rely=0.2, anchor="center")

        # Adicione uma frase
        self.frase_label = tk.Label(self, text="OLÁ, ESCOLHA O QUE DESEJA FAZER", font=("Arial", 18), bg="white")
        self.frase_label.place(relx=0.5, rely=0.4, anchor="center")

        # Botões
        self.button1 = tk.Button(self, text="VER CAMPEONATO", command=self.vercamp, bg="blue", fg="white", font=("Arial", 14))
        self.button1.place(relx=0.3, rely=0.6, anchor="center")

        self.button2 = tk.Button(self, text="DESLOGAR", command=self.fechar_Tela_Editor, bg="red", fg="white", font=("Arial", 14))
        self.button2.place(relx=0.7, rely=0.6, anchor="center")

        # # Botão de voltar
        # self.back_button = tk.Button(self, text="Voltar", command=self.fechar_Tela_Editor, bg="blue", fg="white", font=("Arial", 14))
        # self.back_button.place(relx=0.05, rely=0.05, anchor="center")
        
    def fechar_Tela_Editor(self):
        self.destroy()

    def vercamp(self):
        tela_pesquisar = Tela_Editor_Pesquisar(self.controller, lista_campeonatos)
        tela_pesquisar.mainloop()
