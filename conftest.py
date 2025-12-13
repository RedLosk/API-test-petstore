import pytest
from api_client import PetStoreAPI
import endpoints
import generators

@pytest.fixture
def create_user():
    #Creates a test user
    user = generators.generate_user()
    response = PetStoreAPI.post(endpoints.user_endpoint(), user)
    return response, user

@pytest.fixture
def create_pet():
    #Creates a test pet
    pet = generators.generate_pet()
    response = PetStoreAPI.post(endpoints.pet_endpoint(), pet)
    return response, pet

@pytest.fixture
def create_order():
    #Creates a test order
    order = generators.generate_order()
    response = PetStoreAPI.post(endpoints.store_order(), order)
    return response, order