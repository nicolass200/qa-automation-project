from requests import Response
from api_tests.services.base_service import BaseService


class StoreService(BaseService):

    @classmethod
    def create(cls, order: dict) -> Response:
        return cls.post("/store/order", order)

    @classmethod
    def get_order(cls, order_id: int) -> Response:
        return super().get(f"/store/order/{order_id}")

    @classmethod
    def delete_order(cls, order_id: int) -> Response:
        return super().delete(f"/store/order/{order_id}")