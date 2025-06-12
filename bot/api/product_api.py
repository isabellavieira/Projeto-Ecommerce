import requests
from azure.cosmos import CosmosClient
from bot.config import DefaultConfig
from bot.api.cosmos_connector import container
config = DefaultConfig()
client = CosmosClient(config.COSMOS_URI, config.COSMOS_KEY)
db = client.get_database_client(config.DATABASE_NAME)
container = db.get_container_client(config.CONTAINER_NAME)

class ProductAPI:
    def __init__(self):
        self.config = DefaultConfig()
        self.base_url = f"{self.config.URL_PREFIX}/produtos"

    def get_products(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            return response.json()
        return None
    
    def buscar_produto(self, nome):
        try:
            query = "SELECT * FROM c WHERE CONTAINS(c.productName, @nome)"
            params = [{"name": "@nome", "value": nome}]
            results = list(container.query_items(query=query, parameters=params, enable_cross_partition_query=True))
            return results
        except Exception as e:
            print(f"Erro ao consultar Cosmos DB: {e}")
            return []
    
    def buscar_por_nome(self, nome):
        """Alias para buscar_produto para manter compatibilidade"""
        return self.buscar_produto(nome)
