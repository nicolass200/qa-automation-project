from api_tests.services.store_service import StoreService

ORDER_ID = 4001


def test_create_get_delete_order():
    order = {
        "id": ORDER_ID,
        "petId": 3001,
        "quantity": 1,
        "shipDate": "2026-05-01T00:00:00.000Z",
        "status": "placed",
        "complete": True,
    }

    assert StoreService.create(order).status_code == 200

    response = StoreService.get_order(ORDER_ID)
    assert response.status_code == 200
    assert response.json()["id"] == ORDER_ID

    assert StoreService.delete_order(ORDER_ID).status_code == 200


def test_get_nonexistent_order():
    response = StoreService.get_order(999999999)
    assert response.status_code == 404