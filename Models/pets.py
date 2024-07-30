import re
import sys
import os

path = sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Models.request import *


class Pet:
    @staticmethod
    def find_pet_by_id(id):
        resp = get_method(f'https://petstore.swagger.io/v2/pet/{id}')
        return resp

    @staticmethod
    def add_pet(test_data):
        Pet.validate_pet_data(test_data)
        resp = post_method('https://petstore.swagger.io/v2/pet', test_data)
        return resp

    @staticmethod
    def delete_pet(id):
        url = f'https://petstore.swagger.io/v2/pet/{id}'
        headers = {
            'accept': 'application/json',
            'api_key': '1'
        }

        # Send the DELETE request
        response = requests.delete(url, headers=headers)
        return response.status_code

    @staticmethod
    def update_pet(test_data):
        Pet.validate_pet_data(test_data)
        resp = post_method("https://petstore.swagger.io/v2/pet", test_data)

    @staticmethod
    def upload_pet_image(pet_id, image_path, additional_metadata):
        resp = get_method(f'https://petstore.swagger.io/v2/pet/{pet_id}')
        if "message" in resp:
            raise ValueError("We can't upload a photo for the pet because ID does not exist")

        url = f"https://petstore.swagger.io/v2/pet/{pet_id}/uploadImage"
        file_name = image_path.split('/')[-1]

        files = {
            'file': (file_name, open(image_path, 'rb'), 'image/jpeg')
        }
        data = {
            'additionalMetadata': additional_metadata
        }

        # Perform the POST request
        response = requests.post(url, headers={'accept': 'application/json'}, files=files, data=data)

        return response

    @staticmethod
    def validate_pet_data(pet_data):
        assert isinstance(pet_data['id'], int), "id must be an integer"
        assert isinstance(pet_data['category'], dict), "category must be a dictionary"
        assert isinstance(pet_data['category']['id'], int), "category id must be an integer"
        assert isinstance(pet_data['category']['name'], str), "category name must be a string"
        assert isinstance(pet_data['name'], str), "name must be a string"
        assert isinstance(pet_data['photoUrls'], list), "photoUrls must be a list"
        for url in pet_data['photoUrls']:
            assert isinstance(url, str), "each photoUrl must be a string"
        assert isinstance(pet_data['tags'], list), "tags must be a list"
        for tag in pet_data['tags']:
            assert isinstance(tag, dict), "each tag must be a dictionary"
            assert isinstance(tag['id'], int), "tag id must be an integer"
            assert isinstance(tag['name'], str), "tag name must be a string"
        assert isinstance(pet_data['status'], str), "status must be a string"
        assert pet_data['status'] in ['available', 'pending', 'sold'], "status must be available, pending, or sold"
