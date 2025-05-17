from core.controller import AppController

def iniciar_cli():
    controller = AppController()
    controller.executar()

if __name__ == "__main__":
    iniciar_cli()
