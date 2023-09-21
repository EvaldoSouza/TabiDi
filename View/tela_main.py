import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from View import tela_cadastro
from View import tela_login
from View import display_users

class Tela_Main(tk.Tk):
    def __init__(self, controller):
        tk.Tk.__init__(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        # Geometria básica
        self.geometry("1200x900")
        self.resizable(width="FALSE", height="FALSE")
        self.controller = controller

        for F in (tela_login.Tela_Login, tela_cadastro.Tela_Cadastro):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(tela_login.Tela_Login)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def main_view(self):
        self.title("TaBedi")
        self.mainloop()

    def show_display_users(self):
        self.show_frame(tela_cadastro.Tela_Cadastro)

    def fechar_tela_main(self):
        self.destroy()