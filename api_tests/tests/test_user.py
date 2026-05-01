from api_tests.services.user_service import create_user, get_user, delete_user

def test_create_and_get_user():
    user = {
        "id": 1001,
        "username": "nicolas_test",
        "firstName": "Nicolas",
        "lastName": "Rodrigues",
        "email": "nicolas@test.com",
        "password": "123456",
        "phone": "999999999",
        "userStatus": 1
    }

    response = create_user(user)
    assert response.status_code == 200

    response = get_user(user["username"])
    assert response.status_code == 200
    assert response.json()["username"] == user["username"]

    response = delete_user(user["username"])
    assert response.status_code == 200