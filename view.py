import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        #login fields
        self.label_login = tk.Frame(self, text='Usuario')
        self.label_login.grid(row= 1, column=0)
        
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)
        
        #password fields
        self.label_senha = tk.Frame(self, text='Senha')
        self.label_login.grid(row= 2, column=0)
        
        self.senha_var = tk.StringVar()
        self.senha_entry = ttk.Entry(self, textvariable=self.senha_var, show='*')
        self.senha_entry.grid(row=2, column=1, sticky=tk.NSEW)
        
        self.enter_button = ttk.Button(self, text='Entrar', command=self.enter_button_clicked)
        self.enter_button.grid(row=3, column=1, padx=10)
        
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=4, column=1, sticky=tk.W)
        
    def enter_button_clicked(self):
        if self.controller:
            self.controller.enter_login(self.email_var.get(), self.senha_var())
    
    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'
    
    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')