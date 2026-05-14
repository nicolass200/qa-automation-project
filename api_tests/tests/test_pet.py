from api_tests.services.pet_service import PetService

PET_ID = 3001

def test_create_update_get_pet():
    pet = {
        "id": PET_ID,
        "name": "dog_nicolas",
        "photoUrls": ["string"],
        "status": "available",
    }

    assert PetService.create(pet).status_code == 200

    pet["name"] = "dog_updated"
    assert PetService.update(pet).status_code == 200

    response = PetService.get(PET_ID)
    assert response.status_code == 200
    assert response.json()["name"] == "dog_updated"


def test_get_nonexistent_pet():
    response = PetService.get(999999999)
    assert response.status_code == 404