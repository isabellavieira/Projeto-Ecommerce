from azure.cosmos import CosmosClient
from bot.config import DefaultConfig

config = DefaultConfig()

client = CosmosClient(config.COSMOS_URI, config.COSMOS_KEY)
database = client.get_database_client(config.DATABASE_NAME)
container = database.get_container_client(config.CONTAINER_NAME)