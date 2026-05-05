import pytest
from api_tests.services.user_service import UserService

USER_ID = 2001
USERNAME = "nicolas_test"


@pytest.fixture(autouse=True)
def cleanup():
    yield
    UserService.delete(USERNAME)


def test_create_and_get_user():
    user = {
        "id": USER_ID,
        "username": USERNAME,
        "firstName": "Nicolas",
        "lastName": "Test",
        "email": "nicolas@test.com",
        "password": "123456",
        "phone": "999999999",
        "userStatus": 1,
    }

    assert UserService.create(user).status_code == 200

    response = UserService.get(USERNAME)
    assert response.status_code == 200
    assert response.json()["username"] == USERNAME


def test_get_nonexistent_user():
    response = UserService.get("usuario_que_nao_existe_xyz")
    assert response.status_code == 404