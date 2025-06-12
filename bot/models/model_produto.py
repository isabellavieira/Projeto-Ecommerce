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
        numero_cartao: str,
        data_expiracao: str,
        cvv: str,
        saldo: float,
    ):
        self.product_name = product_name
        self.preco = preco
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
                # Dados mock para teste - em produção viriam do userState
                "nome": "Usuário Teste",
                "email": "teste@email.com",
                "cpf": "123.456.789-00",
                "telefone": "(11) 99999-9999",
                "dtNascimento": "1990-01-01"
            },
            "endereco": {
                # Dados mock para teste
                "logradouro": "Rua Teste",
                "complemento": "Apto 123",
                "bairro": "Centro",
                "cidade": "São Paulo",
                "estado": "SP",
                "cep": "01234-567"
            },
            "cartao": {
                "numero": self.numero_cartao,
                "validade": self.data_expiracao,
                "cvv": self.cvv,
                "saldo": self.saldo,
            },
        }
