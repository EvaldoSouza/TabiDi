from Controller import controller_inicial
from View import tela_login


class Main:
    @staticmethod
    def run():
        #A tela login precisa de um controller
        controler = controller_inicial.ControllerInicial()
        tela = tela_login.TelaLogin(controler)
        tela.login_view()

if __name__ == '__main__':
    Main.run()