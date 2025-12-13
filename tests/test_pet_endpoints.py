import allure
from api_client import PetStoreAPI
import endpoints
import generators

@allure.feature("Pets")
class TestPets:

    @allure.title("Create a pet")
    def test_create_pet(self):
        pet = generators.generate_pet()
        response = PetStoreAPI.post(endpoints.pet_endpoint(), pet)
        assert response.status_code == 200

    @allure.title("Get a pet by ID")
    def test_get_pet(self, create_pet):
        create_response, pet = create_pet

        get_response = PetStoreAPI.get(endpoints.pet_by_id(pet["id"]))
        assert get_response.status_code == 200

    @allure.title("Update pet")
    def test_update_pet(self, create_pet):
        create_response, pet = create_pet

        updated_pet = pet.copy()
        updated_pet["name"] = "Новое Имя"

        response = PetStoreAPI.put(endpoints.pet_endpoint(), updated_pet)
        assert response.status_code == 200

    @allure.title("Delete pet")
    def test_delete_pet(self, create_pet):
        create_response, pet = create_pet
        delete_response = PetStoreAPI.delete(endpoints.pet_by_id(pet["id"]))
        get_response = PetStoreAPI.get(endpoints.pet_by_id(pet["id"]))
        assert get_response.status_code == 404

    @allure.title("Find pets by status")
    def test_find_pets_by_status(self):
        for status in ["available", "pending", "sold"]:
            response = PetStoreAPI.get(
                endpoints.pets_by_status(),
                params={"status": status}
            )
            assert response.status_code == 200