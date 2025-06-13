from azure.cosmos import CosmosClient
from bot.config import DefaultConfig
import requests

config = DefaultConfig()

client = CosmosClient(config.COSMOS_URI, config.COSMOS_KEY)
database = client.get_database_client(config.DATABASE_NAME)
container = database.get_container_client(config.CONTAINER_NAME)

def consultar_pedido_por_id(id_pedido: str) -> dict:
    try:
        response = requests.get(f"http://localhost:8080/api/pedidos/{id_pedido}", timeout=10)

        if response.status_code == 200:
            return response.json()  # Retorna os dados do pedido
        elif response.status_code == 404:
            return None  # Pedido não encontrado
        else:
            raise Exception(f"Erro ao consultar pedido: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Erro ao consultar pedido: {str(e)}")
        return None