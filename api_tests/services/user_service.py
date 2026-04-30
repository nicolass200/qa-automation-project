import requests

BASE_URL = "https://petstore.swagger.io/v2"

def create_user(user_data):
    return requests.post(f"{BASE_URL}/user", json=user_data)

def get_user(username):
    return requests.get(f"{BASE_URL}/user/{username}")

def delete_user(username):
    return requests.delete(f"{BASE_URL}/user/{username}")