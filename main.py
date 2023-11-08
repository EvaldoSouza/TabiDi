from Controller import controller_inicial


class Main:
    @staticmethod
    def run():
        controlador = controller_inicial.ControllerInicial()

        controlador.chama_tela_login()

if __name__ == '__main__':
    Main.run()