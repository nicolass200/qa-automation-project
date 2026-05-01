import requests
from requests import Response
from config import Config


class BaseService:
    """Encapsula chamadas HTTP com timeout e URL base centralizados."""

    BASE_URL = Config.API_BASE_URL
    TIMEOUT = Config.API_TIMEOUT

    @classmethod
    def get(cls, path: str) -> Response:
        return requests.get(f"{cls.BASE_URL}{path}", timeout=cls.TIMEOUT)

    @classmethod
    def post(cls, path: str, data: dict) -> Response:
        return requests.post(f"{cls.BASE_URL}{path}", json=data, timeout=cls.TIMEOUT)

    @classmethod
    def put(cls, path: str, data: dict) -> Response:
        return requests.put(f"{cls.BASE_URL}{path}", json=data, timeout=cls.TIMEOUT)

    @classmethod
    def delete(cls, path: str) -> Response:
        return requests.delete(f"{cls.BASE_URL}{path}", timeout=cls.TIMEOUT)