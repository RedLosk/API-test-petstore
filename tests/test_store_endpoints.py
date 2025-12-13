import allure
from api_client import PetStoreAPI
import endpoints
import generators


@allure.feature("Store")
class TestStore:

    @allure.title("Get inventory")
    def test_get_inventory(self):
        response = PetStoreAPI.get(endpoints.store_inventory())
        assert response.status_code == 200

    @allure.title("Create order")
    def test_create_order(self):
        order = generators.generate_order()
        response = PetStoreAPI.post(endpoints.store_order(), order)
        assert response.status_code == 200

    @allure.title("Get an order by ID")
    def test_get_order(self, create_order):
        create_response, order = create_order
        get_response = PetStoreAPI.get(endpoints.order_by_id(order["id"]))
        assert get_response.status_code == 200

    @allure.title("Delete order")
    def test_delete_order(self, create_order):
        create_response, order = create_order
        delete_response = PetStoreAPI.delete(endpoints.order_by_id(order["id"]))
        get_response = PetStoreAPI.get(endpoints.order_by_id(order["id"]))
        assert get_response.status_code == 404