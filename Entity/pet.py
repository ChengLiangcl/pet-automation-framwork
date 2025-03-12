from util.request import Request

import requests
class Pet():
    def __init__(self): 
        """
        Initialize a Pet object.

        The Pet object is a wrapper around a client object that is used to interact with the Petstore API.
        The client object is an instance of the Request class, which is used to send HTTP requests to the API.

        The Pet object is initialized with a prefix and a request object. The prefix is the relative path of the API endpoint. The request object is used to send HTTP requests to the API.
        """
        self.prefix= '/pet'
        self.request = Request()
    
    def get_pet_by_id(self, pet_id):
        """
        Gets a pet by id.

        Args:
            pet_id (int): The id of the pet to retrieve.

        Returns:
            tuple: A tuple containing the status code (int), the JSON response data (dict), and the response message (str).

        """
        url = f'{self.prefix}/{pet_id}'
        code,data, message = self.request.get_request(url)
        return code, data, message
    
    def create_pet(self, payload):
        """
        Creates a new pet in the pet store.

        Args:
            payload (dict): A dictionary containing the pet data to be created. The payload should include all necessary fields to define a pet.

        Returns:    
            tuple: A tuple containing the status code (int), the JSON response data (dict), and the response message (str).
        """
        code, data,message = self.request.post_request(self.prefix, payload)
        return code, data, message
    def update_pet_with_form_data(self, payload, pet_id):
        
        url = f'{self.prefix}/{pet_id}'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        code, data, message =  self.request.post_request(url, payload, headers)
       
        return code, data, message
    def update_pet(self, payload ):
        code, data,message = self.request.put_request(self.prefix, payload)
        return code, data, message

    def delete_pet(self, pet_id):
        url = f'{self.prefix}/{pet_id}'
        code, data, message = self.request.delete_request(url)
        return code, data, message
    def find_pet_by_status(self, payload):
        url = f'{self.prefix}/findByStatus'
        code,data, message = self.request.get_request(url, payload)
        return code, data, message
    def upload_image(self, pet_id, meta_data, files):
        url = f'https://petstore.swagger.io/v2{self.prefix}/{pet_id}/uploadImage'
        response = requests.post(url, data=meta_data, files=files, headers={'accept': 'application/json'})
        return response.status_code, response.json()

        