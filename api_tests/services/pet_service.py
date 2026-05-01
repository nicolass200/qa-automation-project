import requests

BASE_URL = "https://petstore.swagger.io/v2"

def create_pet(pet_data):
    return requests.post(f"{BASE_URL}/pet", json=pet_data)

def get_pet(pet_id):
    return requests.get(f"{BASE_URL}/pet/{pet_id}")

def update_pet(pet_data):
    return requests.put(f"{BASE_URL}/pet", json=pet_data)