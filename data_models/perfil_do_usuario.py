from botbuilder.schema import Attachment

class PerfilDoUsuario:
    def __init__(self, nome: str = None, idade: int = None, email: str = None, foto_perfil: Attachment = None):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.foto_perfil = foto_perfil

    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "email": self.email,
            "foto_perfil": self.foto_perfil
        }

    @staticmethod
    def from_dict(data: dict):
        return PerfilDoUsuario(
            nome=data.get("nome"),
            idade=data.get("idade"),
            email=data.get("email"),
            foto_perfil=data.get("foto_perfil")
        )