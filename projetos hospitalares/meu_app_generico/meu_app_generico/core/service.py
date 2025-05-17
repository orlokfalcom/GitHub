from core.model import Usuario

class UsuarioService:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, nome, email):
        novo_usuario = Usuario(nome, email)
        self.usuarios.append(novo_usuario)
        return novo_usuario

    def listar_usuarios(self):
        return self.usuarios
