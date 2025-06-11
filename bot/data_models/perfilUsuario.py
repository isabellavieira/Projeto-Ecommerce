from botbuilder.schema import Attachment

class PerfilUsuarioState:
    """
    Estado serializável do usuário, com dados pessoais.
    """
    def __init__(
        self,
        nome: str = None,
        idade: int = 0,
        email: str = None,
        foto_perfil: Attachment = None,
    ):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.foto_perfil = foto_perfil

    def to_dict(self) -> dict:
        """
        Serializa o estado para dicionário.
        """
        return {
            "nome": self.nome,
            "idade": self.idade,
            "email": self.email,
            "foto_perfil": self.foto_perfil,
        }

    @staticmethod
    def from_dict(data: dict) -> "PerfilUsuarioState":
        """
        Desserializa o estado a partir de um dicionário.
        """
        return PerfilUsuarioState(
            nome=data.get("nome"),
            idade=data.get("idade", 0),
            email=data.get("email"),
            foto_perfil=data.get("foto_perfil"),
        )
