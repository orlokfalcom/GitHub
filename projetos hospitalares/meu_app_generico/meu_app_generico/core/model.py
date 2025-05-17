class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __repr__(self):
        return f"Usuario(nome={self.nome}, email={self.email})"
