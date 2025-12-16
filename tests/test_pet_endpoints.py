import allure
from api_client import PetStoreAPI
import endpoints
import generators
from schemas import PET_SCHEMA, PETS_ARRAY_SCHEMA
from validators import validate_schema, validate_response_time, validate_content_type, validate_http_code


@allure.feature("Pets")
class TestPets:

    @allure.title("Create a pet - HTTP code 200")
    def test_create_pet_http_code(self, create_pet):
        create_response, pet = create_pet
        validate_http_code(create_response, 200)

    @allure.title("Create a pet - Content type")
    def test_create_pet_content_type(self, create_pet):
        create_response, pet = create_pet
        validate_content_type(create_response)

    @allure.title("Create a pet - Response time")
    def test_create_pet_response_time(self, create_pet):
        create_response, pet = create_pet
        validate_response_time(create_response)

    @allure.title("Create a pet - Schema validation")
    def test_create_pet_schema(self, create_pet):
        create_response, pet = create_pet
        response_json = create_response.json()
        validate_schema(response_json, PET_SCHEMA)

    @allure.title("Create a pet - ID matches")
    def test_create_pet_id_matches(self, create_pet):
        create_response, pet = create_pet
        response_json = create_response.json()
        assert response_json["id"] == pet["id"]

    @allure.title("Create a pet - Name matches")
    def test_create_pet_name_matches(self, create_pet):
        create_response, pet = create_pet
        response_json = create_response.json()
        assert response_json["name"] == pet["name"]

    @allure.title("Create a pet - Status matches")
    def test_create_pet_status_matches(self, create_pet):
        create_response, pet = create_pet
        response_json = create_response.json()
        assert response_json["status"] == pet["status"]

    @allure.title("Get a pet by ID - HTTP code 200")
    def test_get_pet_http_code(self, create_pet):
        create_response, pet = create_pet
        get_response = PetStoreAPI.get(endpoints.pet_by_id(pet["id"]))
        validate_http_code(get_response, 200)

    @allure.title("Get a pet by ID - Content type")
    def test_get_pet_content_type(self, create_pet):
        create_response, pet = create_pet
        get_response = PetStoreAPI.get(endpoints.pet_by_id(pet["id"]))
        validate_content_type(get_response)

    @allure.title("Get a pet by ID - Response time")
    def test_get_pet_response_time(self, create_pet):
        create_response, pet = create_pet
        get_response = PetStoreAPI.get(endpoints.pet_by_id(pet["id"]))
        validate_response_time(get_response)

    @allure.title("Get a pet by ID - Schema validation")
    def test_get_pet_schema(self, create_pet):
        create_response, pet = create_pet
        get_response = PetStoreAPI.get(endpoints.pet_by_id(pet["id"]))
        response_json = get_response.json()
        validate_schema(response_json, PET_SCHEMA)

    @allure.title("Get a pet by ID - ID matches")
    def test_get_pet_id_matches(self, create_pet):
        create_response, pet = create_pet
        get_response = PetStoreAPI.get(endpoints.pet_by_id(pet["id"]))
        response_json = get_response.json()
        assert response_json["id"] == pet["id"]

    @allure.title("Get a pet by ID - Name matches")
    def test_get_pet_name_matches(self, create_pet):
        create_response, pet = create_pet
        get_response = PetStoreAPI.get(endpoints.pet_by_id(pet["id"]))
        response_json = get_response.json()
        assert response_json["name"] == pet["name"]

    @allure.title("Update pet - HTTP code 200")
    def test_update_pet_http_code(self, create_pet):
        create_response, pet = create_pet
        updated_pet = pet.copy()
        updated_pet["name"] = "UpdatedName"
        response = PetStoreAPI.put(endpoints.pet_endpoint(), updated_pet)
        validate_http_code(response, 200)

    @allure.title("Update pet - Content type")
    def test_update_pet_content_type(self, create_pet):
        create_response, pet = create_pet
        updated_pet = pet.copy()
        updated_pet["name"] = "UpdatedName"
        response = PetStoreAPI.put(endpoints.pet_endpoint(), updated_pet)
        validate_content_type(response)

    @allure.title("Update pet - Response time")
    def test_update_pet_response_time(self, create_pet):
        create_response, pet = create_pet
        updated_pet = pet.copy()
        updated_pet["name"] = "UpdatedName"
        response = PetStoreAPI.put(endpoints.pet_endpoint(), updated_pet)
        validate_response_time(response)

    @allure.title("Update pet - Schema validation")
    def test_update_pet_schema(self, create_pet):
        create_response, pet = create_pet
        updated_pet = pet.copy()
        updated_pet["name"] = "UpdatedName"
        response = PetStoreAPI.put(endpoints.pet_endpoint(), updated_pet)
        response_json = response.json()
        validate_schema(response_json, PET_SCHEMA)

    @allure.title("Update pet - Name updated")
    def test_update_pet_name_updated(self, create_pet):
        create_response, pet = create_pet
        updated_pet = pet.copy()
        updated_pet["name"] = "UpdatedName"
        response = PetStoreAPI.put(endpoints.pet_endpoint(), updated_pet)
        response_json = response.json()
        assert response_json["name"] == "UpdatedName"

    @allure.title("Delete pet - HTTP code 200")
    def test_delete_pet_http_code(self, create_pet):
        create_response, pet = create_pet
        delete_response = PetStoreAPI.delete(endpoints.pet_by_id(pet["id"]))
        validate_http_code(delete_response, 200)

    @allure.title("Delete pet - Content type")
    def test_delete_pet_content_type(self, create_pet):
        create_response, pet = create_pet
        delete_response = PetStoreAPI.delete(endpoints.pet_by_id(pet["id"]))
        validate_content_type(delete_response)

    @allure.title("Delete pet - Pet not found after delete")
    def test_delete_pet_not_found(self, create_pet):
        create_response, pet = create_pet
        PetStoreAPI.delete(endpoints.pet_by_id(pet["id"]))
        get_response = PetStoreAPI.get(endpoints.pet_by_id(pet["id"]))
        validate_http_code(get_response, 404)

    @allure.title("Find pets by status available - HTTP code 200")
    def test_find_pets_by_status_available_http_code(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "available"}
        )
        validate_http_code(response, 200)

    @allure.title("Find pets by status available - Content type")
    def test_find_pets_by_status_available_content_type(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "available"}
        )
        validate_content_type(response)

    @allure.title("Find pets by status available - Response time")
    def test_find_pets_by_status_available_response_time(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "available"}
        )
        validate_response_time(response)

    @allure.title("Find pets by status available - Schema validation")
    def test_find_pets_by_status_available_schema(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "available"}
        )
        pets = response.json()
        validate_schema(pets, PETS_ARRAY_SCHEMA)

    @allure.title("Find pets by status available - All pets have correct status")
    def test_find_pets_by_status_available_all_pets_status(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "available"}
        )
        pets = response.json()
        assert all(pet["status"] == "available" for pet in pets)

    @allure.title("Find pets by status pending - HTTP code 200")
    def test_find_pets_by_status_pending_http_code(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "pending"}
        )
        validate_http_code(response, 200)

    @allure.title("Find pets by status pending - Content type")
    def test_find_pets_by_status_pending_content_type(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "pending"}
        )
        validate_content_type(response)

    @allure.title("Find pets by status pending - Response time")
    def test_find_pets_by_status_pending_response_time(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "pending"}
        )
        validate_response_time(response)

    @allure.title("Find pets by status pending - Schema validation")
    def test_find_pets_by_status_pending_schema(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "pending"}
        )
        pets = response.json()
        validate_schema(pets, PETS_ARRAY_SCHEMA)

    @allure.title("Find pets by status pending - All pets have correct status")
    def test_find_pets_by_status_pending_all_pets_status(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "pending"}
        )
        pets = response.json()
        assert all(pet["status"] == "pending" for pet in pets)

    @allure.title("Find pets by status sold - HTTP code 200")
    def test_find_pets_by_status_sold_http_code(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "sold"}
        )
        validate_http_code(response, 200)

    @allure.title("Find pets by status sold - Content type")
    def test_find_pets_by_status_sold_content_type(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "sold"}
        )
        validate_content_type(response)

    @allure.title("Find pets by status sold - Response time")
    def test_find_pets_by_status_sold_response_time(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "sold"}
        )
        validate_response_time(response)

    @allure.title("Find pets by status sold - Schema validation")
    def test_find_pets_by_status_sold_schema(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "sold"}
        )
        pets = response.json()
        validate_schema(pets, PETS_ARRAY_SCHEMA)

    @allure.title("Find pets by status sold - All pets have correct status")
    def test_find_pets_by_status_sold_all_pets_status(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "sold"}
        )
        pets = response.json()
        assert all(pet["status"] == "sold" for pet in pets)

    @allure.title("Get non-existent pet - HTTP code 200")
    def test_get_nonexistent_pet_http_code(self):
        response = PetStoreAPI.get(endpoints.pet_by_id(999999999))
        validate_http_code(response, 200)

    @allure.title("Get non-existent pet - Content type")
    def test_get_nonexistent_pet_content_type(self):
        response = PetStoreAPI.get(endpoints.pet_by_id(999999999))
        validate_content_type(response)

    @allure.title("Get non-existent pet - Response time")
    def test_get_nonexistent_pet_response_time(self):
        response = PetStoreAPI.get(endpoints.pet_by_id(999999999))
        validate_response_time(response)

    @allure.title("Get non-existent pet - Schema validation")
    def test_get_nonexistent_pet_schema(self):
        response = PetStoreAPI.get(endpoints.pet_by_id(999999999))
        response_json = response.json()
        validate_schema(response_json, PET_SCHEMA)

    @allure.title("Get non-existent pet - ID matches")
    def test_get_nonexistent_pet_id_matches(self):
        response = PetStoreAPI.get(endpoints.pet_by_id(999999999))
        response_json = response.json()
        assert response_json["id"] == 999999999

    @allure.title("Create pet with invalid data - HTTP code 500")
    def test_create_pet_invalid_data_http_code(self):
        invalid_pet = generators.generate_invalid_pet()
        response = PetStoreAPI.post(endpoints.pet_endpoint(), invalid_pet)
        validate_http_code(response, 500)

    @allure.title("Create pet with invalid data - Content type")
    def test_create_pet_invalid_data_content_type(self):
        invalid_pet = generators.generate_invalid_pet()
        response = PetStoreAPI.post(endpoints.pet_endpoint(), invalid_pet)
        validate_content_type(response)

    @allure.title("Create pet with invalid data - Response time")
    def test_create_pet_invalid_data_response_time(self):
        invalid_pet = generators.generate_invalid_pet()
        response = PetStoreAPI.post(endpoints.pet_endpoint(), invalid_pet)
        validate_response_time(response)

    @allure.title("PUT creates new pet for non-existent ID - HTTP code 200")
    def test_put_creates_new_pet_http_code(self):
        new_pet = generators.generate_pet_with_custom_id(888888888)
        response = PetStoreAPI.put(endpoints.pet_endpoint(), new_pet)
        validate_http_code(response, 200)
        PetStoreAPI.delete(endpoints.pet_by_id(new_pet["id"]))

    @allure.title("PUT creates new pet for non-existent ID - Content type")
    def test_put_creates_new_pet_content_type(self):
        new_pet = generators.generate_pet_with_custom_id(888888888)
        response = PetStoreAPI.put(endpoints.pet_endpoint(), new_pet)
        validate_content_type(response)
        PetStoreAPI.delete(endpoints.pet_by_id(new_pet["id"]))

    @allure.title("PUT creates new pet for non-existent ID - Response time")
    def test_put_creates_new_pet_response_time(self):
        new_pet = generators.generate_pet_with_custom_id(888888888)
        response = PetStoreAPI.put(endpoints.pet_endpoint(), new_pet)
        validate_response_time(response)
        PetStoreAPI.delete(endpoints.pet_by_id(new_pet["id"]))

    @allure.title("PUT creates new pet for non-existent ID - Schema validation")
    def test_put_creates_new_pet_schema(self):
        new_pet = generators.generate_pet_with_custom_id(888888888)
        response = PetStoreAPI.put(endpoints.pet_endpoint(), new_pet)
        response_json = response.json()
        validate_schema(response_json, PET_SCHEMA)
        PetStoreAPI.delete(endpoints.pet_by_id(new_pet["id"]))

    @allure.title("PUT creates new pet for non-existent ID - ID matches")
    def test_put_creates_new_pet_id_matches(self):
        new_pet = generators.generate_pet_with_custom_id(888888888)
        response = PetStoreAPI.put(endpoints.pet_endpoint(), new_pet)
        response_json = response.json()
        assert response_json["id"] == new_pet["id"]
        PetStoreAPI.delete(endpoints.pet_by_id(new_pet["id"]))

    @allure.title("PUT creates new pet for non-existent ID - Name matches")
    def test_put_creates_new_pet_name_matches(self):
        new_pet = generators.generate_pet_with_custom_id(888888888)
        response = PetStoreAPI.put(endpoints.pet_endpoint(), new_pet)
        response_json = response.json()
        assert response_json["name"] == new_pet["name"]
        PetStoreAPI.delete(endpoints.pet_by_id(new_pet["id"]))

    @allure.title("Find pets by invalid status - HTTP code 200")
    def test_find_pets_by_invalid_status_http_code(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "invalid_status_xyz"}
        )
        validate_http_code(response, 200)

    @allure.title("Find pets by invalid status - Content type")
    def test_find_pets_by_invalid_status_content_type(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "invalid_status_xyz"}
        )
        validate_content_type(response)

    @allure.title("Find pets by invalid status - Response time")
    def test_find_pets_by_invalid_status_response_time(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "invalid_status_xyz"}
        )
        validate_response_time(response)

    @allure.title("Find pets by invalid status - Returns list")
    def test_find_pets_by_invalid_status_returns_list(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "invalid_status_xyz"}
        )
        pets = response.json()
        assert isinstance(pets, list)

    @allure.title("Find pets by invalid status - Returns empty array")
    def test_find_pets_by_invalid_status_returns_empty(self):
        response = PetStoreAPI.get(
            endpoints.pets_by_status(),
            params={"status": "invalid_status_xyz"}
        )
        pets = response.json()
        assert len(pets) == 0
