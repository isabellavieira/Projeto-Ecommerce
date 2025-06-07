import requests
import config
from config import DefaultConfig

class ProductAPI:
    def __init__(self):
        self.config = DefaultConfig()
        self.base_url = self.config.PRODUCT_API_URL

    def get_product(self, product_id):
        url = f"{self.base_url}/products/{product_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()[0]
        else:
            return None

    def search_product(self, product_name):
        url = f"{self.base_url}/products/search"
        params = {"name": product_name}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None