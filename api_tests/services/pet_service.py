from requests import Response
from api_tests.services.base_service import BaseService


class PetService(BaseService):

    @classmethod
    def create(cls, pet: dict) -> Response:
        return cls.post("/pet", pet)

    @classmethod
    def get(cls, pet_id: int) -> Response:
        return super().get(f"/pet/{pet_id}")

    @classmethod
    def update(cls, pet: dict) -> Response:
        return cls.put("/pet", pet)