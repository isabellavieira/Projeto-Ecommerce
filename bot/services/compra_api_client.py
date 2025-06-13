import requests
import json

async def enviar_compra(payload: dict) -> tuple:
    try:
        response = requests.post("http://localhost:8080/api/compras", json=payload, timeout=10)
        if response.status_code == 200:
            response_data = response.json()
            sucesso = response_data.get("sucesso", False)
            mensagem = response_data.get("mensagem", "")
            idPedido = response_data.get("idPedido", None)
            return sucesso, mensagem, idPedido
        elif response.status_code == 400:
            response_data = response.json()
            return False, response_data.get("mensagem", "Erro desconhecido"), None
        else:
            return False, f"Erro do servidor: {response.status_code} - {response.text}", None
    except Exception as e:
        return False, f"Erro inesperado: {str(e)}", None
