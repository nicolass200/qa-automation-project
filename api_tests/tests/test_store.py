from api_tests.services.store_service import create_order, get_order, delete_order

def test_create_get_delete_order():
    order = {
        "id": 4001,
        "petId": 3001,
        "quantity": 1,
        "shipDate": "2026-05-01T00:00:00.000Z",
        "status": "placed",
        "complete": True
    }

    response = create_order(order)
    assert response.status_code == 200

    response = get_order(order["id"])
    assert response.status_code == 200
    assert response.json()["id"] == order["id"]

    response = delete_order(order["id"])
    assert response.status_code == 200