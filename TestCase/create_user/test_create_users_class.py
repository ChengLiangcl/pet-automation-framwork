import json
import pytest
import allure
from Models.users import User


@pytest.mark.run(order=1)
class TestCreateUsers:
    @allure.title(""""
                Scenario: Create a new user account
                Given the user is not logged in
                When the user sends a POST request to create a new account with valid details
                Then the account should be created successfully
                And the user should receive a confirmation message
                And the backend will return a response with code 200, type and user id""")
    def test_create_users_with_valid_data(self):
        with open('TestCase/create_user/test_data/create_user_with_valid_data.json', 'r') as file:
            data = json.load(file)
        user = User()
        response = user.create_user(data)
        assert response['code'] == 200
        assert response['message'] == '119'

    @allure.title(""""
                Scenario: Create a new user account 
                Given the user is not logged in 
                When the user sends a POST request to create a new account with invalid details (empty data) 
                Then the account won't be created successfully 
                And the api automation will throw an error message""")
    def test_create_users_with_invalid_data_when_test_data_is_empty(self):
        with pytest.raises(ValueError, match="id is missing from the data"):
            user = User()
            user.create_user({})

    @allure.title(""""
                Scenario: Create a new user account 
                Given the user is not logged in 
                When the user sends a POST request to create a new account with invalid details (wrong data type for 
                phone & username)
                Then the account won't be created successfully 
                And the api automation will throw an error message""")
    def test_create_users_with_invalid_data_phone_and_username_is_not_string(self):
        with open('TestCase/create_user/test_data/create_user_with_wrong_data_type_phone_and_username.json',
                  'r') as file:
            data = json.load(file)
        with pytest.raises(ValueError, match="username should be of type str, but got list"):
            user = User()
            user.create_user(data)

    @allure.title(""""
                Scenario: Create a new user account
                Given the user is not logged in
                When the user sends a POST request to create a new account with invalid email
                Then the account won't be created successfully
                And the api automation code will throw an error message""")
    def test_create_users_with_invalid_data_when_email_is_invalid(self):
        with open('TestCase/create_user/test_data/create_user_with_invalid_email.json', 'r') as file:
            data = json.load(file)
            with pytest.raises(ValueError, match="email has an invalid email format"):
                user = User()
                user.create_user(data)

    @allure.title(""""
                Scenario: Create a new user account
                Given the user is not logged in
                When the user sends a POST request to create a new account with existing username
                Then the account won't be created successfully
                And the api automation code will throw an error message""")
    def test_create_users_with_invalid_data_when_username_already_existed(self):
        with open('TestCase/create_user/test_data/create_user_with_existed_username.json', 'r') as file:
            data = json.load(file)
            user = User()
            with pytest.raises(ValueError, match="The username already exists"):
                if user.get_user_by_name(data['username'])['username'] == data['username']:
                    raise ValueError('The username already exists')

    @allure.title("Create a new user named jackie chan")
    def test_crete_user_named_jackie_chan(self):
        with open('TestCase/create_user/test_data/create_user_with_name_jakie_chan.json', 'r') as file:
            data = json.load(file)
        user = User()
        response = user.create_user(data)
        assert response['code'] == 200
        assert response['message'] == '5111'

    @allure.title(""""
                Given the user is not logged in
                When the admin creates multiple user accounts with valid data
                Then multiple user accounts will be created successfully
                And the admin searches for the newly added users and their data will be returned
                """)
    def test_create_multiple_users(self):
        with open('TestCase/create_user/test_data/bulk_upload_user.json', 'r') as file:
            data = json.load(file)
            user = User()
            response = user.bulk_create_users_with_list(data)
            assert response['code'] == 200

    def test_list_new_created_users(self):
        with open('TestCase/create_user/test_data/bulk_upload_user.json', 'r') as file:
            data = json.load(file)
            user_name_one = data[0]['username']
            user_name_two = data[1]['username']
            user_name_three = data[2]['username']

            user = User()
            resp = user.get_user_by_name(user_name_one)
            assert user_name_one == resp['username']

            resp = user.get_user_by_name(user_name_two)
            assert user_name_two == resp['username']

            resp = user.get_user_by_name(user_name_three)
            assert user_name_three == resp['username']

    @allure.title(""""
                Given the user is not logged in
                When the admin creates multiple user accounts with invalid data
                Then multiple user accounts will not be created successfully
                And error will be raised at this time
                """)
    def test_create_multiple_users_with_invalid_data(self):
        with open('TestCase/create_user/test_data/bulk_upload_invalid.json', 'r') as file:
            data = json.load(file)
            user = User()
            with pytest.raises(ValueError, match="id should be of type int, but got str"):
                user.bulk_create_users_with_list(data)

