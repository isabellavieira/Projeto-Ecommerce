from botbuilder.schema import Attachment
import re
from datetime import datetime

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
        dt_nascimento: str = None,
    ):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.foto_perfil = foto_perfil
        self.set_dt_nascimento(dt_nascimento)

    def to_dict(self) -> dict:
        """
        Serializa o estado para dicionário.
        """
        return {
            "nome": self.nome,
            "idade": self.idade,
            "email": self.email,
            "foto_perfil": self.foto_perfil,
            "dt_nascimento": self.dt_nascimento,
        }

    @staticmethod
    def from_dict(data: dict) -> "PerfilUsuarioState":
        """
        Desserializa o estado a partir de um dicionário.
        """
        estado = PerfilUsuarioState(
            nome=data.get("nome"),
            idade=data.get("idade", 0),
            email=data.get("email"),
            foto_perfil=data.get("foto_perfil"),
        )
        estado.set_dt_nascimento(data.get("dt_nascimento"))
        return estado

    def set_dt_nascimento(self, dt_nascimento: str):
        try:
            self.dt_nascimento = datetime.strptime(dt_nascimento, "%Y-%m-%d").date()
        except ValueError:
            self.dt_nascimento = datetime(1990, 1, 1).date()  # Fallback

    def validar_cpf(cpf: str) -> bool:
        return re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf) is not None

    def validar_telefone(telefone: str) -> bool:
        return re.match(r"^\(\d{2}\) \d{4,5}-\d{4}$", telefone) is not None
