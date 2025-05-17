from core.service import UsuarioService

class AppController:
    def __init__(self):
        self.usuario_service = UsuarioService()

    def executar(self):
        print("Aplicativo iniciado.")
        self.usuario_service.adicionar_usuario("João", "joao@email.com")
        for user in self.usuario_service.listar_usuarios():
            print(user)
