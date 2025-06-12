# bot/models/model_produto.py

class ModeloComprarProduto:
    """
    Modelo de dados para representar a compra de um produto.
    Usado pelo diálogo para montar o payload JSON que será enviado ao back-end.
    """

    def __init__(
        self,
        product_name: str,
        preco: float,
        usuario: dict,
        endereco: dict,
        numero_cartao: str,
        data_expiracao: str,
        cvv: str,
        saldo: float,
    ):
        self.product_name = product_name
        self.preco = preco
        self.usuario = usuario
        self.endereco = endereco
        self.numero_cartao = numero_cartao
        self.data_expiracao = data_expiracao
        self.cvv = cvv
        self.saldo = saldo

    def to_payload(self) -> dict:
        """
        Constrói o corpo de requisição conforme o DTO CompraRequest do back-end Java.
        """
        return {
            "productName": self.product_name,
            "preco": self.preco,
            "usuario": {
                "nome": self.usuario.get("nome"),
                "email": self.usuario.get("email"),
                "cpf": self.usuario.get("cpf"),
                "telefone": self.usuario.get("telefone"),
                "dtNascimento": self.usuario.get("dtNascimento"),
            },
            "endereco": {
                "logradouro": self.endereco.get("logradouro"),
                "complemento": self.endereco.get("complemento"),
                "bairro": self.endereco.get("bairro"),
                "cidade": self.endereco.get("cidade"),
                "estado": self.endereco.get("estado"),
                "cep": self.endereco.get("cep"),
            },
            "cartao": {
                "numero": self.numero_cartao,
                "validade": self.data_expiracao,
                "cvv": self.cvv,
                "saldo": self.saldo,
            },
        }
