from azure.cosmos import CosmosClient
from bot.config import DefaultConfig
from bot.api.cosmos_connector import container
config = DefaultConfig()
client = CosmosClient(config.COSMOS_URI, config.COSMOS_KEY)
db = client.get_database_client(config.DATABASE_NAME)
container = db.get_container_client(config.CONTAINER_NAME)

class ProductAPI:
    def buscar_por_nome(self, nome):
        try:
            query = "SELECT * FROM c WHERE CONTAINS(c.productName, @nome)"
            params = [{"name": "@nome", "value": nome}]
            results = list(container.query_items(query=query, parameters=params, enable_cross_partition_query=True))
            return results
        except Exception as e:
            print(f"Erro ao consultar Cosmos DB: {e}")
            return []
