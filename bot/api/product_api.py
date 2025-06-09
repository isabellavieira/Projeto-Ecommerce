from azure.cosmos import CosmosClient
from bot.config import DefaultConfig

config = DefaultConfig()
client = CosmosClient(config.COSMOS_URI, config.COSMOS_KEY)
db = client.get_database_client(config.DATABASE_NAME)
container = db.get_container_client(config.CONTAINER_NAME)

class ProductAPI:
    def get_products(self):
        query = "SELECT * FROM c"
        results = list(container.query_items(query=query, enable_cross_partition_query=True))
        if results:
            return results[0]  # simplificação: pega o primeiro resultado
        return {}