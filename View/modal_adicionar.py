import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk

class Modal_Adicionar(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.resizable(width="TRUE", height="TRUE")
        self.title("Editor - Adicionar")

        #informação
        self.frase_label = tk.Label(self, text="ADICIONAR INFORMAÇÃO", font=("Arial", 18), )
        self.frase_label.place(relx=0.5, rely=0.3, anchor="center")
        
        self.informacao_var = tk.StringVar()
        self.entry_informacao = tk.Entry(self, font=("Arial", 14), textvariable=self.informacao_var)
        self.entry_informacao.place(relx=0.5, rely=0.45, anchor="center")

        # Botão de adicionar
        self.confirmar_button = tk.Button(self, text="Confirmar", command=self.confirmar, bg="green", fg="black", font=("Arial", 14))
        self.confirmar_button.place(relx=0.5, rely=0.7, anchor="se")

        # Botão de voltar
        self.voltar_button = tk.Button(self, text="Voltar", command=self.voltar, bg="blue", fg="black", font=("Arial", 14))
        self.voltar_button.place(relx=0.65, rely=0.7, anchor="se")

    def confirmar(self):
        pass
    
    def voltar(self):
        self.destroy()