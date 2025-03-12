from entity.pet import Pet
import allure
import pytest
import json
#This is the test class for positive cases

test_data = ''
# Open and load the JSON data
with open('pet_test_case/pet_positive_case_test_data.json', 'r') as file:
    test_data = json.load(file)

pet = Pet()


class TestPetAPIPositive():
    allure.description('This test cases will test whole life cycle for creating pets, updating pets, fetching pets and delete pets')
    
    def test_create_pet(self):
        #test create pet API
        payload = test_data['create_pet_data']
        code, data, message = pet.create_pet(payload)
        assert code == 200, "Failed to create pet, please make sure all the inputs are valid"
        assert data['id'] ==  payload['id']
        assert data['category']['id'] ==  payload['category']['id']
        assert data['category']['name'] ==  payload['category']['name']
        assert data['photoUrls'][0] ==  payload['photoUrls'][0]
        assert data['tags'][0]['id'] ==  payload['tags'][0]['id']
        assert data['tags'][0]['name'] ==  payload['tags'][0]['name']
        assert data['status'] ==  payload['status']
        
        #Fetch the pet record which just created, verify all values are matched 
        code, data, message = pet.get_pet_by_id(payload['id'])
        assert code == 200, "Failed to fetch pet, please make sure pet id does exist"
        assert data['id'] ==  payload['id']
        assert data['category']['id'] ==  payload['category']['id']
        assert data['category']['name'] ==  payload['category']['name']
        assert data['photoUrls'][0] ==  payload['photoUrls'][0]
        assert data['tags'][0]['id'] ==  payload['tags'][0]['id']
        assert data['tags'][0]['name'] ==  payload['tags'][0]['name']
        assert data['status'] ==  payload['status']
    
    def test_update_pet(self):
        payload = test_data['create_pet_data']
        copy_payload = payload
        copy_payload['id'] = 789456
        code, data, message = pet.update_pet(copy_payload)
        assert code == 200, "Failed to update the existing pet record"
        assert data['id'] == copy_payload['id'], "Failed to update the record, please check the payload"
                
        
    # def test_pet_create_delete_update_get_life_cycle(self):
    
    def test_update_pet_with_form(self):
        payload = test_data['create_pet_data']
        code, data, message = pet.update_pet_with_form_data({'name':'test_pet', 'status':'sold'}, '911119')
        assert code ==200, "Failed to update pet data with form data"
        assert data['message'] == '911119'
        
    def test_upload_image(self):
        
        additional_metadata = {'additionalMetadata': 'this is for extra info'}
        file_path = 'pet_test_case/tree.jpg'
        with open(file_path, 'rb') as file:
            files = {
                'file': ('tree.jpg', file, 'image/jpeg') 
            }
            code, data = pet.upload_image( '911119', additional_metadata, files)
        assert code == 200

        
    
    def test_find_by_status(self):
        code, data, message = pet.find_pet_by_status({'status':'available'})
        assert code ==200
        code, data, message = pet.find_pet_by_status({'status':'pending'})
        assert code ==200
        code, data, message = pet.find_pet_by_status({'status':'sold'})
        assert code ==200
    
    
    def test_clean_up_record(self):
        code, data, message = pet.delete_pet('789456')
        assert code ==200, "Failed to delete the record, please make sure the id exist"
        code, data, message = pet.delete_pet('911119')
        assert code ==200, "Failed to delete the record, please make sure the id exist"
        