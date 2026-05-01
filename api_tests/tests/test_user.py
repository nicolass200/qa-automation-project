import pytest
from api_tests.services.user_service import UserService

# ID único por módulo evita colisão em execuções paralelas
USER_ID = 2001


@pytest.fixture(autouse=True)
def cleanup():
    """Garante limpeza mesmo se o teste falhar."""
    yield
    UserService.delete("nicolas_test")


def test_create_and_get_user():
    user = {
        "id": USER_ID,
        "username": "nicolas_test",
        "firstName": "Nicolas",
        "lastName": "Test",
        "email": "nicolas@test.com",
        "password": "123456",
        "phone": "999999999",
        "userStatus": 1,
    }

    assert UserService.create(user).status_code == 200

    response = UserService.get(user["username"])
    assert response.status_code == 200
    assert response.json()["username"] == user["username"]


def test_get_nonexistent_user():
    response = UserService.get("usuario_que_nao_existe_xyz")
    assert response.status_code == 404