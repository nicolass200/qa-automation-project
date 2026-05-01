from api_tests.services.pet_service import create_pet, get_pet, update_pet

def test_create_update_get_pet():
    pet = {
        "id": 3001,
        "name": "dog_nicolas",
        "photoUrls": ["string"],
        "status": "available"
    }

    # Criar pet
    response = create_pet(pet)
    assert response.status_code == 200

    # Atualizar pet
    pet["name"] = "dog_updated"
    response = update_pet(pet)
    assert response.status_code == 200

    # Buscar pet
    response = get_pet(pet["id"])
    assert response.status_code == 200
    assert response.json()["name"] == "dog_updated"