import requests
import config import DefaultConfig

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