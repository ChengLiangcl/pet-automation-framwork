import re
import sys
import os

path = sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Models.request import *


# Add the top-level directory of your project to sys.path

class User:
    # {
    #     "id": 0,
    #     "username": "string",
    #     "firstName": "string",
    #     "lastName": "string",
    #     "email": "string",
    #     "password": "string",
    #     "phone": "string",
    #     "userStatus": 0
    # }
    # def __init__(self, id, user_name, first_name, last_name, email, password, phone, user_status):
    #     self.id = id
    #     self.user_name = user_name
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.email = email
    #     self.password = password
    #     self.phone = phone
    #     self.user_status = user_status

    @staticmethod
    def get_user_by_name(user_name):
        api = f"https://petstore.swagger.io/v2/user/{user_name}"
        user_info = get_method(api)
        return user_info

    @staticmethod
    def create_user(test_data):
        # defined the dict key
        reference_key = {
            "id": "int",
            "username": "string",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
        }

        # Validate the user input
        # case 1, the user input should be dictionary, if it is not a dictionary then return the error
        if not isinstance(test_data, dict):
            raise ValueError("The input data is not dictionary")
        else:
            User.validate_user_data(test_data)
        result = post_method("https://petstore.swagger.io/v2/user", test_data)
        return result

    @staticmethod
    def delete_user(user_name):
        url = f"https://petstore.swagger.io/v2/user/{user_name}"
        response = delete_method(url)
        return response

    @staticmethod
    def update_user(user_name, update_data):
        url = f'https://petstore.swagger.io/v2/user/{user_name}'
        response = put_method(url, update_data)
        return response

    @staticmethod
    def validate_user_data(data):
        expected_types = {
            "id": int,
            "username": str,
            "firstName": str,
            "lastName": str,
            "email": str,
            "password": str,
            "phone": str,
            "userStatus": int
        }

        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        for key, expected_type in expected_types.items():
            if key in data:
                if not isinstance(data[key], expected_type):
                    raise ValueError(
                        f"{key} should be of type {expected_type.__name__}, but got {type(data[key]).__name__}")
                if key == "email" and not re.match(email_regex, data['email']):
                    raise ValueError(f"{key} has an invalid email format")
            else:
                raise ValueError(f"{key} is missing from the data")

    @staticmethod
    def login(username, password):
        api = f'https://petstore.swagger.io/v2/user/login?username={username}&password={password}'
        headers = {
            'Accept': 'application/json'
        }
        user_info = User.get_user_by_name(username)['data']

        if 'type' in user_info:
            raise ValueError('username does not exist in the database, please create an account first')
        else:
            if user_info['password'] == password and user_info['username'] == username:
                response = get_method(api)
                return response

            else:
                raise ValueError('Password was incorrect, please try it again')

    @staticmethod
    def logout():
        api = f'https://petstore.swagger.io/v2/user/logout'
        response = get_method(api)
        return response

    @staticmethod
    def bulk_create_users_with_array(user_list):
        # check if the input is valid
        for user in user_list:
            User.validate_user_data(user)
        response = post_method('https://petstore.swagger.io/v2/user/createWithArray', user_list)
        return  response

    @staticmethod
    def bulk_create_users_with_list(user_list):
        # check if the input is valid
        for user in user_list:
            User.validate_user_data(user)
        response = post_method('https://petstore.swagger.io/v2/user/createWithList', user_list)
        return response
