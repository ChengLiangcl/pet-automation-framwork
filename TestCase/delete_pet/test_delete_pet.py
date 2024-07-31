import json
import pytest
import allure
from Models.pets import Pet


@pytest.mark.run(order=20)
class TestDeletePet:

    @allure.title(""""
    Scenario: Delete a pet by ID
    Given the user is logged in
    When the user sends a request to delete a pet with a valid ID
    Then the pet is deleted successfully""")
    def test_delete_pet_with_valid_id(self):
        pet = Pet()
        resp = pet.delete_pet(10)
        status_code = resp['status_code']
        assert status_code == 200

    @allure.title(""""
        Attempt to delete a pet that does not exist
        Given the user is logged in
        When the user sends a request to delete a pet with an invalid ID
        Then the deletion fails
        And the user receives an error message indicating the pet was not found""")
    def test_delete_pet_with_non_exist_data(self):
        pet = Pet()
        resp = pet.delete_pet(5555555)
        status_code = resp['status_code']
        assert status_code == 404
