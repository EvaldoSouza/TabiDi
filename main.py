from View import tela_login
import tkinter


class Main:
    @staticmethod
    def run(root):
        #A tela login precisa de um controller
        tela = tela_login.TelaLogin(root)
        tela.login_view()

if __name__ == '__main__':
    root = tkinter.Tk()
    root.withdraw()
    Main.run(root)
    root.destroy()