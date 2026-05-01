from requests import Response
from api_tests.services.base_service import BaseService


class UserService(BaseService):

    @classmethod
    def create(cls, user: dict) -> Response:
        return cls.post("/user", user)

    @classmethod
    def get(cls, username: str) -> Response:
        return super().get(f"/user/{username}")

    @classmethod
    def delete(cls, username: str) -> Response:
        return super().delete(f"/user/{username}")