from Controller import controller

from Controller import teste

class Main:
    @staticmethod
    def run():
        controlador = controller.Controller()

        controlador.main_controller()

if __name__ == '__main__':
    Main.run()