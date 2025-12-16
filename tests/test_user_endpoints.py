import allure
from api_client import PetStoreAPI
import endpoints
import generators
from schemas import USER_SCHEMA, SUCCESS_RESPONSE_SCHEMA
from validators import validate_schema, validate_response_time, validate_content_type, validate_http_code


@allure.feature("Users")
class TestUsers:

    @allure.title("Create user - HTTP code 200")
    def test_create_user_http_code(self, create_user):
        create_response, user = create_user
        validate_http_code(create_response, 200)

    @allure.title("Create user - Content type")
    def test_create_user_content_type(self, create_user):
        create_response, user = create_user
        validate_content_type(create_response)

    @allure.title("Create user - Response time")
    def test_create_user_response_time(self, create_user):
        create_response, user = create_user
        validate_response_time(create_response)

    @allure.title("Create user - Schema validation")
    def test_create_user_schema(self, create_user):
        create_response, user = create_user
        response_json = create_response.json()
        validate_schema(response_json, SUCCESS_RESPONSE_SCHEMA)

    @allure.title("Create user - Code is 200")
    def test_create_user_code_200(self, create_user):
        create_response, user = create_user
        response_json = create_response.json()
        assert response_json["code"] == 200

    @allure.title("Get user - HTTP code 200")
    def test_get_user_http_code(self, create_user):
        create_response, user = create_user
        get_response = PetStoreAPI.get(endpoints.user_by_username(user["username"]))
        validate_http_code(get_response, 200)

    @allure.title("Get user - Content type")
    def test_get_user_content_type(self, create_user):
        create_response, user = create_user
        get_response = PetStoreAPI.get(endpoints.user_by_username(user["username"]))
        validate_content_type(get_response)

    @allure.title("Get user - Response time")
    def test_get_user_response_time(self, create_user):
        create_response, user = create_user
        get_response = PetStoreAPI.get(endpoints.user_by_username(user["username"]))
        validate_response_time(get_response)

    @allure.title("Get user - Schema validation")
    def test_get_user_schema(self, create_user):
        create_response, user = create_user
        get_response = PetStoreAPI.get(endpoints.user_by_username(user["username"]))
        response_json = get_response.json()
        validate_schema(response_json, USER_SCHEMA)

    @allure.title("Get user - Username matches")
    def test_get_user_username_matches(self, create_user):
        create_response, user = create_user
        get_response = PetStoreAPI.get(endpoints.user_by_username(user["username"]))
        response_json = get_response.json()
        assert response_json["username"] == user["username"]

    @allure.title("Update user - HTTP code 200")
    def test_update_user_http_code(self, create_user):
        create_response, user = create_user
        updated_user = user.copy()
        updated_user["firstName"] = "UpdatedName"
        response = PetStoreAPI.put(
            endpoints.user_by_username(user["username"]),
            updated_user
        )
        validate_http_code(response, 200)

    @allure.title("Update user - Content type")
    def test_update_user_content_type(self, create_user):
        create_response, user = create_user
        updated_user = user.copy()
        updated_user["firstName"] = "UpdatedName"
        response = PetStoreAPI.put(
            endpoints.user_by_username(user["username"]),
            updated_user
        )
        validate_content_type(response)

    @allure.title("Update user - Response time")
    def test_update_user_response_time(self, create_user):
        create_response, user = create_user
        updated_user = user.copy()
        updated_user["firstName"] = "UpdatedName"
        response = PetStoreAPI.put(
            endpoints.user_by_username(user["username"]),
            updated_user
        )
        validate_response_time(response)

    @allure.title("Delete user - HTTP code 200")
    def test_delete_user_http_code(self, create_user):
        create_response, user = create_user
        delete_response = PetStoreAPI.delete(endpoints.user_by_username(user["username"]))
        validate_http_code(delete_response, 200)

    @allure.title("Delete user - Content type")
    def test_delete_user_content_type(self, create_user):
        create_response, user = create_user
        delete_response = PetStoreAPI.delete(endpoints.user_by_username(user["username"]))
        validate_content_type(delete_response)

    @allure.title("Delete user - User not found after delete")
    def test_delete_user_not_found(self, create_user):
        create_response, user = create_user
        PetStoreAPI.delete(endpoints.user_by_username(user["username"]))
        get_response = PetStoreAPI.get(endpoints.user_by_username(user["username"]))
        validate_http_code(get_response, 404)

    @allure.title("User login - HTTP code 200")
    def test_login_http_code(self, create_user):
        create_response, user = create_user
        response = PetStoreAPI.get(
            endpoints.user_login(),
            params={
                "username": user["username"],
                "password": user["password"]
            }
        )
        validate_http_code(response, 200)

    @allure.title("User login - Content type")
    def test_login_content_type(self, create_user):
        create_response, user = create_user
        response = PetStoreAPI.get(
            endpoints.user_login(),
            params={
                "username": user["username"],
                "password": user["password"]
            }
        )
        validate_content_type(response)

    @allure.title("User login - Response time")
    def test_login_response_time(self, create_user):
        create_response, user = create_user
        response = PetStoreAPI.get(
            endpoints.user_login(),
            params={
                "username": user["username"],
                "password": user["password"]
            }
        )
        validate_response_time(response)

    @allure.title("User login - Schema validation")
    def test_login_schema(self, create_user):
        create_response, user = create_user
        response = PetStoreAPI.get(
            endpoints.user_login(),
            params={
                "username": user["username"],
                "password": user["password"]
            }
        )
        response_json = response.json()
        validate_schema(response_json, SUCCESS_RESPONSE_SCHEMA)

    @allure.title("User logout - HTTP code 200")
    def test_logout_http_code(self):
        response = PetStoreAPI.get(endpoints.user_logout())
        validate_http_code(response, 200)

    @allure.title("User logout - Content type")
    def test_logout_content_type(self):
        response = PetStoreAPI.get(endpoints.user_logout())
        validate_content_type(response)

    @allure.title("User logout - Response time")
    def test_logout_response_time(self):
        response = PetStoreAPI.get(endpoints.user_logout())
        validate_response_time(response)

    @allure.title("User logout - Response contains message")
    def test_logout_contains_message(self):
        response = PetStoreAPI.get(endpoints.user_logout())
        response_json = response.json()
        assert "message" in response_json

    @allure.title("Get non-existent user - HTTP code 404")
    def test_get_nonexistent_user_http_code(self):
        response = PetStoreAPI.get(
            endpoints.user_by_username("nonexistent_user_12345")
        )
        validate_http_code(response, 404)

    @allure.title("Get non-existent user - Content type")
    def test_get_nonexistent_user_content_type(self):
        response = PetStoreAPI.get(
            endpoints.user_by_username("nonexistent_user_12345")
        )
        validate_content_type(response)

    @allure.title("Get non-existent user - Response time")
    def test_get_nonexistent_user_response_time(self):
        response = PetStoreAPI.get(
            endpoints.user_by_username("nonexistent_user_12345")
        )
        validate_response_time(response)

    @allure.title("Get non-existent user - Response type is error")
    def test_get_nonexistent_user_type_error(self):
        response = PetStoreAPI.get(
            endpoints.user_by_username("nonexistent_user_12345")
        )
        response_json = response.json()
        assert response_json["type"] == "error"

    @allure.title("PUT creates new user for non-existent username - HTTP code 200")
    def test_put_creates_new_user_http_code(self):
        new_user = generators.generate_user_with_custom_data(
            777777777, "new_user_test", "new@test.com", "password123"
        )
        response = PetStoreAPI.put(
            endpoints.user_by_username("new_user_test"),
            new_user
        )
        validate_http_code(response, 200)
        PetStoreAPI.delete(endpoints.user_by_username("new_user_test"))

    @allure.title("PUT creates new user for non-existent username - Content type")
    def test_put_creates_new_user_content_type(self):
        new_user = generators.generate_user_with_custom_data(
            777777777, "new_user_test", "new@test.com", "password123"
        )
        response = PetStoreAPI.put(
            endpoints.user_by_username("new_user_test"),
            new_user
        )
        validate_content_type(response)
        PetStoreAPI.delete(endpoints.user_by_username("new_user_test"))

    @allure.title("PUT creates new user for non-existent username - Response time")
    def test_put_creates_new_user_response_time(self):
        new_user = generators.generate_user_with_custom_data(
            777777777, "new_user_test", "new@test.com", "password123"
        )
        response = PetStoreAPI.put(
            endpoints.user_by_username("new_user_test"),
            new_user
        )
        validate_response_time(response)
        PetStoreAPI.delete(endpoints.user_by_username("new_user_test"))

    @allure.title("PUT creates new user for non-existent username - Schema validation")
    def test_put_creates_new_user_schema(self):
        new_user = generators.generate_user_with_custom_data(
            777777777, "new_user_test", "new@test.com", "password123"
        )
        response = PetStoreAPI.put(
            endpoints.user_by_username("new_user_test"),
            new_user
        )
        response_json = response.json()
        validate_schema(response_json, SUCCESS_RESPONSE_SCHEMA)
        PetStoreAPI.delete(endpoints.user_by_username("new_user_test"))

    @allure.title("PUT creates new user for non-existent username - Code is 200")
    def test_put_creates_new_user_code_200(self):
        new_user = generators.generate_user_with_custom_data(
            777777777, "new_user_test", "new@test.com", "password123"
        )
        response = PetStoreAPI.put(
            endpoints.user_by_username("new_user_test"),
            new_user
        )
        response_json = response.json()
        assert response_json["code"] == 200
        PetStoreAPI.delete(endpoints.user_by_username("new_user_test"))

    @allure.title("Login with wrong credentials - HTTP code 200")
    def test_login_wrong_credentials_http_code(self):
        response = PetStoreAPI.get(
            endpoints.user_login(),
            params={"username": "wrong", "password": "wrong"}
        )
        validate_http_code(response, 200)

    @allure.title("Login with wrong credentials - Content type")
    def test_login_wrong_credentials_content_type(self):
        response = PetStoreAPI.get(
            endpoints.user_login(),
            params={"username": "wrong", "password": "wrong"}
        )
        validate_content_type(response)

    @allure.title("Login with wrong credentials - Response time")
    def test_login_wrong_credentials_response_time(self):
        response = PetStoreAPI.get(
            endpoints.user_login(),
            params={"username": "wrong", "password": "wrong"}
        )
        validate_response_time(response)

    @allure.title("Login with wrong credentials - Schema validation")
    def test_login_wrong_credentials_schema(self):
        response = PetStoreAPI.get(
            endpoints.user_login(),
            params={"username": "wrong", "password": "wrong"}
        )
        response_json = response.json()
        validate_schema(response_json, SUCCESS_RESPONSE_SCHEMA)
