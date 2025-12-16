import allure
from api_client import PetStoreAPI
import endpoints
import generators
from schemas import INVENTORY_SCHEMA, SUCCESS_RESPONSE_SCHEMA
from validators import validate_schema, validate_response_time, validate_content_type, validate_http_code


@allure.feature("Store")
class TestStore:

    @allure.title("Get inventory - HTTP code 200")
    def test_get_inventory_http_code(self):
        response = PetStoreAPI.get(endpoints.store_inventory())
        validate_http_code(response, 200)

    @allure.title("Get inventory - Content type")
    def test_get_inventory_content_type(self):
        response = PetStoreAPI.get(endpoints.store_inventory())
        validate_content_type(response)

    @allure.title("Get inventory - Response time")
    def test_get_inventory_response_time(self):
        response = PetStoreAPI.get(endpoints.store_inventory())
        validate_response_time(response)

    @allure.title("Get inventory - Schema validation")
    def test_get_inventory_schema(self):
        response = PetStoreAPI.get(endpoints.store_inventory())
        inventory = response.json()
        validate_schema(inventory, INVENTORY_SCHEMA)

    @allure.title("Get inventory - Total pets is non-negative")
    def test_get_inventory_total_pets_non_negative(self):
        response = PetStoreAPI.get(endpoints.store_inventory())
        inventory = response.json()
        total_pets = sum(inventory.values())
        assert total_pets >= 0

    @allure.title("Create order - HTTP code 200")
    def test_create_order_http_code(self, create_order):
        create_response, order = create_order
        validate_http_code(create_response, 200)

    @allure.title("Create order - Content type")
    def test_create_order_content_type(self, create_order):
        create_response, order = create_order
        validate_content_type(create_response)

    @allure.title("Create order - Response time")
    def test_create_order_response_time(self, create_order):
        create_response, order = create_order
        validate_response_time(create_response)

    @allure.title("Create order - ID matches")
    def test_create_order_id_matches(self, create_order):
        create_response, order = create_order
        response_json = create_response.json()
        assert response_json["id"] == order["id"]

    @allure.title("Create order - Pet ID matches")
    def test_create_order_pet_id_matches(self, create_order):
        create_response, order = create_order
        response_json = create_response.json()
        assert response_json["petId"] == order["petId"]

    @allure.title("Create order - Status is placed")
    def test_create_order_status_placed(self, create_order):
        create_response, order = create_order
        response_json = create_response.json()
        assert response_json["status"] == "placed"

    @allure.title("Get an order by ID - HTTP code 200")
    def test_get_order_http_code(self, create_order):
        create_response, order = create_order
        get_response = PetStoreAPI.get(endpoints.order_by_id(order["id"]))
        validate_http_code(get_response, 200)

    @allure.title("Get an order by ID - Content type")
    def test_get_order_content_type(self, create_order):
        create_response, order = create_order
        get_response = PetStoreAPI.get(endpoints.order_by_id(order["id"]))
        validate_content_type(get_response)

    @allure.title("Get an order by ID - Response time")
    def test_get_order_response_time(self, create_order):
        create_response, order = create_order
        get_response = PetStoreAPI.get(endpoints.order_by_id(order["id"]))
        validate_response_time(get_response)

    @allure.title("Get an order by ID - ID matches")
    def test_get_order_id_matches(self, create_order):
        create_response, order = create_order
        get_response = PetStoreAPI.get(endpoints.order_by_id(order["id"]))
        response_json = get_response.json()
        assert response_json["id"] == order["id"]

    @allure.title("Get an order by ID - Pet ID matches")
    def test_get_order_pet_id_matches(self, create_order):
        create_response, order = create_order
        get_response = PetStoreAPI.get(endpoints.order_by_id(order["id"]))
        response_json = get_response.json()
        assert response_json["petId"] == order["petId"]

    @allure.title("Delete order - HTTP code 200")
    def test_delete_order_http_code(self, create_order):
        create_response, order = create_order
        delete_response = PetStoreAPI.delete(endpoints.order_by_id(order["id"]))
        validate_http_code(delete_response, 200)

    @allure.title("Delete order - Content type")
    def test_delete_order_content_type(self, create_order):
        create_response, order = create_order
        delete_response = PetStoreAPI.delete(endpoints.order_by_id(order["id"]))
        validate_content_type(delete_response)

    @allure.title("Delete order - Order not found after delete")
    def test_delete_order_not_found(self, create_order):
        create_response, order = create_order
        PetStoreAPI.delete(endpoints.order_by_id(order["id"]))
        get_response = PetStoreAPI.get(endpoints.order_by_id(order["id"]))
        validate_http_code(get_response, 404)

    @allure.title("Get non-existent order - HTTP code 404")
    def test_get_nonexistent_order_http_code(self):
        response = PetStoreAPI.get(endpoints.order_by_id(999999999))
        validate_http_code(response, 404)

    @allure.title("Get non-existent order - Content type")
    def test_get_nonexistent_order_content_type(self):
        response = PetStoreAPI.get(endpoints.order_by_id(999999999))
        validate_content_type(response)

    @allure.title("Get non-existent order - Response time")
    def test_get_nonexistent_order_response_time(self):
        response = PetStoreAPI.get(endpoints.order_by_id(999999999))
        validate_response_time(response)

    @allure.title("Delete non-existent order - HTTP code 404")
    def test_delete_nonexistent_order_http_code(self):
        response = PetStoreAPI.delete(endpoints.order_by_id(999999999))
        validate_http_code(response, 404)

    @allure.title("Delete non-existent order - Content type")
    def test_delete_nonexistent_order_content_type(self):
        response = PetStoreAPI.delete(endpoints.order_by_id(999999999))
        validate_content_type(response)

    @allure.title("Delete non-existent order - Response time")
    def test_delete_nonexistent_order_response_time(self):
        response = PetStoreAPI.delete(endpoints.order_by_id(999999999))
        validate_response_time(response)

    @allure.title("Create order with non-existent pet - HTTP code 200")
    def test_create_order_nonexistent_pet_http_code(self):
        order = generators.generate_order_with_pet_id(999999999)
        response = PetStoreAPI.post(endpoints.store_order(), order)
        validate_http_code(response, 200)

    @allure.title("Create order with non-existent pet - Content type")
    def test_create_order_nonexistent_pet_content_type(self):
        order = generators.generate_order_with_pet_id(999999999)
        response = PetStoreAPI.post(endpoints.store_order(), order)
        validate_content_type(response)

    @allure.title("Create order with non-existent pet - Response time")
    def test_create_order_nonexistent_pet_response_time(self):
        order = generators.generate_order_with_pet_id(999999999)
        response = PetStoreAPI.post(endpoints.store_order(), order)
        validate_response_time(response)

    @allure.title("Create order with non-existent pet - Pet ID matches")
    def test_create_order_nonexistent_pet_pet_id_matches(self):
        order = generators.generate_order_with_pet_id(999999999)
        response = PetStoreAPI.post(endpoints.store_order(), order)
        response_json = response.json()
        assert response_json["petId"] == 999999999
