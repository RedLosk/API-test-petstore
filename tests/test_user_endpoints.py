import allure
from api_client import PetStoreAPI
import endpoints
import generators

@allure.feature("Users")
class TestUsers:
    @allure.title("Create user")
    def test_create_user(self):
        user = generators.generate_user()
        response = PetStoreAPI.post(endpoints.user_endpoint(), user)
        assert response.status_code == 200

    @allure.title("Get user")
    def test_get_user(self, create_user):
        create_response, user = create_user
        get_response = PetStoreAPI.get(endpoints.user_by_username(user["username"]))
        assert get_response.status_code == 200

    @allure.title("Update user")
    def test_update_user(self, create_user):
        create_response, user = create_user
        updated_user = user.copy()
        updated_user["firstName"] = "Обновленное Имя"

        response = PetStoreAPI.put(
            endpoints.user_by_username(user["username"]),
            updated_user
        )
        assert response.status_code == 200

    @allure.title("Delete user")
    def test_delete_user(self, create_user):
        create_response, user = create_user
        delete_response = PetStoreAPI.delete(endpoints.user_by_username(user["username"]))
        get_response = PetStoreAPI.get(endpoints.user_by_username(user["username"]))
        assert get_response.status_code == 404

    @allure.title("User login")
    def test_login(self, create_user):
        create_response, user = create_user

        response = PetStoreAPI.get(
            endpoints.user_login(),
            params={
                "username": user["username"],
                "password": user["password"]
            }
        )
        assert response.status_code == 200

    @allure.title("User logout")
    def test_logout(self):
        response = PetStoreAPI.get(endpoints.user_logout())
        assert response.status_code == 200