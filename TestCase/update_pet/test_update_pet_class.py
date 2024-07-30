import pytest
import allure
from Models.pets import Pet


@pytest.mark.run(order=9)
class TestUpdatePet:

    @allure.title(""""
    Scenario: Update a pet with valid data
    Given the user is logged in
    When the user sends a request to update a pet with valid data
    Then the pet is updated successfully
    And the user receives a confirmation message with the updated pet details""")
    def test_update_pet_with_valid_data(self):
        pass

    @allure.title(""""
      Given the user is logged in
      When the user sends a request to update a pet with invalid data (e.g., invalid status)
      Then the update fails 
      And the user receives an error message indicating the invalid data""")
    def test_update_pet_with_invalid_data(self):
        pass

    @allure.title("""
        Scenario: Attempt to update a pet that does not exist
        Given the user is logged in
        When the user sends a request to update a pet with an invalid ID
        Then the update fails
        And the user receives an error message indicating the pet was not found""")
    def test_update_non_exist_pet(self):
        pass

    @allure.title("""
        Scenario Update a pet with missing required fields
        Given the user is logged in
        When the user sends a request to update a pet with missing required fields
        Then the update fails
        And it will raise an error to indicate the missing fields""")
    def test_update_missing_field_pet(self):
        pass
