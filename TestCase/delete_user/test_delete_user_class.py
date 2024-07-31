import json
import pytest
import allure
from Models.users import User


@pytest.mark.run(order=21)
class TestDeleteUsers:
    @allure.title(""""
                Scenario: delete an account
                Given the user created an account
                When the user sends a delete request to delete an existing account with valid username 
                Then the account should be removed successfully 
                And the user won't be able to login into the system
                And admin won't be able to find the user by username""")
    def test_delete_user_with_valid_username(self):
        with open('TestCase/delete_user/test_data/delete_user.json', 'r') as file:
            data = json.load(file)
        user = User()
        response = user.delete_user(data['username'])
        status_code = response['status_code']
        assert status_code == 200

    @allure.title(""""
                 Scenario: delete an account
                 Given the user created an account
                 When the user sends a delete request to delete an existing account with valid username 
                 Then the account should be removed successfully 
                 And the user won't be able to login into the system
                 And admin won't be able to find the user by username""")
    def test_delete_non_exist_user(self):
        with open('TestCase/delete_user/test_data/delete_non_exist_user.json', 'r') as file:
            data = json.load(file)
        user = User()
        response = user.delete_user(data)
        status_code = response['status_code']
        assert status_code == 404
