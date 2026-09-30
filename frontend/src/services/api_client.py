import requests
from utils.config import API_BASE_URL


class APIClient:

    def __init__(self):
        self.session = requests.Session()

    def post(self, endpoint: str, **kwargs):
        return self.session.post(
            f"{API_BASE_URL}{endpoint}",
            **kwargs
        )

    def get(self, endpoint: str, **kwargs):
        return self.session.get(
            f"{API_BASE_URL}{endpoint}",
            **kwargs
        )

    def put(self, endpoint: str, **kwargs):
        return self.session.put(
            f"{API_BASE_URL}{endpoint}",
            **kwargs
        )

    def delete(self, endpoint: str, **kwargs):
        return self.session.delete(
            f"{API_BASE_URL}{endpoint}",
            **kwargs
        )


api_client = APIClient()