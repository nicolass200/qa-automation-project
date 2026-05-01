import requests

BASE_URL = "https://petstore.swagger.io/v2"

def create_order(order_data):
    return requests.post(f"{BASE_URL}/store/order", json=order_data)

def get_order(order_id):
    return requests.get(f"{BASE_URL}/store/order/{order_id}")

def delete_order(order_id):
    return requests.delete(f"{BASE_URL}/store/order/{order_id}")