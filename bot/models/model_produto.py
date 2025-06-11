# bot/models/model_produto.py

class ModeloComprarProduto:
    """
    Modelo de dados para representar a compra de um produto.
    Usado pelo diálogo para montar o payload JSON que será enviado ao back-end.
    """

    def __init__(
        self,
        product_id: int,
        numero_cartao: str,
        data_expiracao: str,
        cvv: str,
        saldo: float,
    ):
        self.product_id = product_id
        self.numero_cartao = numero_cartao
        self.data_expiracao = data_expiracao
        self.cvv = cvv
        self.saldo = saldo

    def to_payload(self) -> dict:
        """
        Constrói o corpo de requisição conforme o DTO CompraRequest do back-end Java.
        """
        return {
            "productName": self.product_id,
            "preco": self.saldo,  # ou ajustar para o preço real se quiser usar
            "usuario": {
                # se tiver userState, você pode preencher aqui
                # "nome": "...",
                # "email": "...",
                # "cpf": "...",
                # "telefone": "...",
            },
            "endereco": {
                # similar ao usuário, se quiser associar endereço
            },
            "cartao": {
                "numero": self.numero_cartao,
                "validade": self.data_expiracao,
                "cvv": self.cvv,
                "saldo": self.saldo,
            },
        }
