import allure
import api_client
import endpoints

@allure.feature("Negative cases")
class TestNegative:

    @allure.title("Get a non-existent user")
    def test_get_nonexistent_user(self):
        response = api_client.PetStoreAPI.get(endpoints.user_by_username("nonexistent_user"))
        assert response.status_code == 404

    @allure.title("Get a non-existent pets")
    def test_get_nonexistent_pet(self):
        response = api_client.PetStoreAPI.get(endpoints.pet_by_id(999999999))
        assert response.status_code == 404

    @allure.title("Delete a non-existent order")
    def test_delete_nonexistent_order(self):
        response = api_client.PetStoreAPI.delete(endpoints.order_by_id(999999999))
        assert response.status_code == 404

    @allure.title("Login with incorrect data")
    def test_login_with_wrong_credentials(self):
        response = api_client.PetStoreAPI.get(
            endpoints.user_login(),
            params={"username": "wrong", "password": "wrong"}
        )
        assert response.status_code == 200