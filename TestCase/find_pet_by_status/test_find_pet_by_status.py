import pytest
import allure
from Models.pets import Pet


@pytest.mark.run(order=10)
class TestFindPetByStatus:
    @allure.title(""""
     Given a logged-in user or admin user ,
     When the user sends a request to find pets by status (the status is 'pending', 'sold', 'available'),
     Then the API should return a list of pets matching the given status.""")
    def test_find_pet_with_valid_status(self):
        pet = Pet()
        sold_result = pet.find_pet_by_status('sold')['status_code']
        assert sold_result == 200

        pending_result = pet.find_pet_by_status('pending')['status_code']
        assert pending_result == 200

        available_result = pet.find_pet_by_status('available')['status_code']
        assert available_result == 200

    @allure.title(""""
      Given an invalid status,
      When the user sends a request to find pets by that status,
      Then the API should return an error message indicating the invalid status.""")
    def test_find_pet_with_invalid_status(self):
        pet = Pet()
        with pytest.raises(AssertionError, match="status must be 'available', 'pending', or 'sold'"):
            pet.find_pet_by_status('sdasdasdasd')

        with pytest.raises(AssertionError, match="status must be a string"):
            pet.find_pet_by_status(11)

        with pytest.raises(AssertionError, match="status must be a string"):
            pet.find_pet_by_status([])
