import tkinter as tk
from tkinter import PhotoImage

class Tela_User(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        #Geometria básica
        self.geometry("900x600")
        self.resizable(width=False, height=False)
        # Adicionando uma imagem de fundo
        self.background_image = PhotoImage(file="View/football_background.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Adicionando uma logo
        self.logo_image = PhotoImage(file="View/sigma.png")
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.place(relx=0.5, rely=0.2, anchor="center")

        # Botão de voltar
        self.back_button = tk.Button(self, text="Voltar", command=self.fechar_Tela_User, bg="yellow", fg="white", font=("Arial", 14))
        self.back_button.place(relx=0.05, rely=0.05,anchor="center")
        
    def fechar_Tela_User(self):
        self.destroy()
