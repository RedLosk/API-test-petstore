import requests
import allure

class PetStoreAPI:
    @staticmethod
    @allure.step("Send a POST request")
    def post(url, data=None):
        return requests.post(url, json=data)

    @staticmethod
    @allure.step("Send a GET request")
    def get(url, params=None):
        return requests.get(url, params=params)

    @staticmethod
    @allure.step("Send a PUT request")
    def put(url, data=None):
        return requests.put(url, json=data)

    @staticmethod
    @allure.step("Send a DELETE request")
    def delete(url):
        return requests.delete(url)