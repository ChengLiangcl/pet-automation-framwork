import json
import pytest
import allure
from Models.users import User


@pytest.mark.run(order=2)
class TestGetUserClass:
    @allure.title(""""
    Scenario: Admin try to retrieve a user by username
    Given the Admin is already at the listing page
    When the Admin sends a GET request with a valid username
    Then the user details should be returned from backend with json data with id, username,first name, last name, email, password, phone and user status
    Then the backend will return the response code 200""")
    def test_get_user_with_valid_username(self):
        with open('TestCase/get_user/test_data/get_user_data.json', 'r') as file:
            data = json.load(file)
        user = User()
        response = user.get_user_by_name(data['username'])
        assert response == {
            "id": 119,
            "username": "jason.liang",
            "firstName": "Jason",
            "lastName": "Liang",
            "email": "jason.liang@humanforce.com",
            "password": "testing123",
            "phone": "00000000",
            "userStatus": 1
        }

    @allure.title(""""
   Scenario: Admin try to retrieve a user by username
   Given the Admin is already at the listing page
   When the Admin sends a GET request with a invalid username
   Then the user details should be returned from backend with json data {code": 1, "type": "error", "message": "User not found"}
   And the admin fail to find a matched user""")
    def test_get_user_with_invalid_username(self):
        with open('TestCase/get_user/test_data/get_user_data.json', 'r') as file:
            data = json.load(file)
        user = User()
        response = user.get_user_by_name(data['invalid_username'])
        assert response['code'] == 1
        assert response['type'] == "error"
        assert response['message'] == "User not found"
