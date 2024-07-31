import json
import pytest
import allure
from Models.users import User


@pytest.mark.run(order=4)
class TestUserLogin:
    @allure.title(""""
                Scenario: User login
                Given an existing user
                When the user provides valid username and password
                Then the user should be logged into the system successfully 
                """)
    def test_user_login_with_correct_username_password(self):
        with open('TestCase/user_login/test_data/correct_username_password.json', 'r') as file:
            data = json.load(file)
        user = User()
        username = data['username']
        password = data['password']
        response = user.login(username, password)
        assert response['status_code'] == 200

    @allure.title(""""
                Scenario: User login
                Given an existing user
                When the user provides invalid username and password
                Then the user should not be logged into the system 
                """)
    def test_user_login_with_wrong_password(self):
        with open('TestCase/user_login/test_data/invalid_password.json', 'r') as file:
            data = json.load(file)
        user = User()
        username = data['username']
        password = data['password']
        with pytest.raises(ValueError, match="Password was incorrect, please try it again"):
            user.login(username, password)

    @allure.title(""""
                Scenario: User login
                Given an existing user
                When the user provides a username which does not exist
                Then the user should not be logged into the system 
                """)
    def test_user_login_with_non_existing_user(self):
        user = User()
        with pytest.raises(ValueError, match="username does not exist in the database, please create an account first"):
            user.login('111111', '121212121')
