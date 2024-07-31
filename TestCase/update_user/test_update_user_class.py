import json
import pytest
import allure
from Models.users import User


@pytest.mark.run(order=3)
class TestUpdateUser:
    @allure.title(""""
                Scenario: Update user info
                Given an existing user
                When the admin sends a delete request to update an existing account with valid username 
                Then the account will be updated successfully
                """)
    def test_update_user_with_valid_test_data(self):
        with open('TestCase/update_user/test_data/update_user.json', 'r') as file:
            data = json.load(file)
        user = User()
        response = user.update_user(data['username'], data)
        status_code = response['status_code']
        data = response['data']
        assert status_code == 200
        assert data['message'] == '5111'

    @allure.title(""""
                Scenario: Get user info after updating
                Given an user finishing updating info
                When the admin update a user account with valid username
                Then the admin should be able to see the updated info
                """)
    def test_verify_updated_user_info(self):
        user = User()
        response = user.get_user_by_name('jackie.chan')
        assert response['data'] == {
            "id": 5111,
            "username": "jackie.chan",
            "firstName": "Jackie",
            "lastName": "Chan",
            "email": "jackie.chan@hmovie.com",
            "password": "testing",
            "phone": "911",
            "userStatus": 0
        }
