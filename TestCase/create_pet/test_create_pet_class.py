import json
import pytest
import allure
from Models.pets import Pet


@pytest.mark.run(order=6)
class TestCreatePet:

    @allure.title(""""
      Scenario: Add a pet with valid data to the store
      Given the user provides valid pet data
      When the user sends a request to create a pet
     Then the pet is created successfully""")
    def test_create_pet_with_valid_data(self):
        pet = Pet()
        with open('TestCase/create_pet/test_data/pet_data.json', 'r') as file:
            data = json.load(file)
        response = pet.add_pet(data)
        response['id'] = 1667
        response['category']['name'] = 'Test_Pet_1'

    @allure.title(""""
      Scenario: Add a pet with invalid data to the store
      Given the user provides invalid pet data
      When the user sends a request to create a pet
      Then the pet won't be created successfully
      And it will raise an error""")
    def test_create_pet_with_invalid_data(self):
        pet = Pet()
        with open('TestCase/create_pet/test_data/pet_data_invalid.json', 'r') as file:
            data = json.load(file)
        with pytest.raises(AssertionError, match="category id must be an integer"):
            pet.add_pet(data)
