import sys
import os

path = sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Models.request import *


class Pet:
    @staticmethod
    def find_pet_by_status(status):
        # Validate the status input
        assert isinstance(status, str), "status must be a string"
        assert status in ['available', 'pending', 'sold'], "status must be 'available', 'pending', or 'sold'"
        try:
            resp = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}')
            return resp.status_code

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

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
        id = test_data['id']
        resp = get_method(f'https://petstore.swagger.io/v2/pet/{id}')
        if "message" in resp and resp["message"] == 'Pet not found':
            raise ValueError("We can't update info for the pet because ID does not exist")

        resp = post_method("https://petstore.swagger.io/v2/pet", test_data)
        return resp

    @staticmethod
    def upload_pet_image(pet_id, image_path, additional_metadata):
        resp = get_method(f'https://petstore.swagger.io/v2/pet/{pet_id}')
        if "message" in resp and resp["message"] == 'Pet not found':
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
        assert 'id' in pet_data, "id field is missing"
        assert isinstance(pet_data['id'], int), "id must be an integer"
        # Validate 'category' field
        category = pet_data.get('category')
        assert category is not None, "category field is missing"
        assert isinstance(category, dict), "category must be a dictionary"
        assert 'id' in category, "category id field is missing"
        assert isinstance(category['id'], int), "category id must be an integer"
        assert 'name' in category, "category name field is missing"
        assert isinstance(category['name'], str), "category name must be a string"

        # Validate 'name' field
        assert 'name' in pet_data, "name field is missing"
        assert isinstance(pet_data['name'], str), "name must be a string"

        # Validate 'photoUrls' field
        photo_urls = pet_data.get('photoUrls')
        assert photo_urls is not None, "photoUrls field is missing"
        assert isinstance(photo_urls, list), "photoUrls must be a list"
        for url in photo_urls:
            assert isinstance(url, str), "each photoUrl must be a string"

        # Validate 'tags' field
        tags = pet_data.get('tags')
        assert tags is not None, "tags field is missing"
        assert isinstance(tags, list), "tags must be a list"
        for tag in tags:
            assert isinstance(tag, dict), "each tag must be a dictionary"
            assert 'id' in tag, "tag id field is missing"
            assert isinstance(tag['id'], int), "tag id must be an integer"
            assert 'name' in tag, "tag name field is missing"
            assert isinstance(tag['name'], str), "tag name must be a string"

        # Validate 'status' field
        assert 'status' in pet_data, "status field is missing"
        assert isinstance(pet_data['status'], str), "status must be a string"
        assert pet_data['status'] in ['available', 'pending', 'sold'], "status must be available, pending, or sold"
