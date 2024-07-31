import json
import pytest
import allure
from Models.store import Store
from Models.pets import Pet


@pytest.mark.run(order=16)
class TestCreateOrder:

    @allure.title(""""
      Scenario: Create an order
        Given the user is authenticated
        When the user creates an order with valid details
        Then the system should return the created order details
        And the status code should be 200 
        And the response should include correct details""")
    def test_create_pet_with_valid_data(self):
        with open('TestCase/create_order/test_data/valid_order.json', 'r') as file:
            data = json.load(file)
            store = Store()
            resp = store.create_order(data)
            assert resp['data']['id'] == 10
            assert resp['status_code'] == 200

    @allure.title(""""
         Scenario: Create an order
        Given the user is authenticated
        When the user creates an order with invalid details (missing fields required)
        Then the system will be failed to crete order details
        And it will raise an error""")
    def test_create_pet_with_invalid_data_missing_pet_id(self):
        with open('TestCase/create_order/test_data/invalid_missing_pet_id_field.json', 'r') as file:
            data = json.load(file)
            store = Store()
            with pytest.raises(ValueError, match="Missing key: petId"):
                store.create_order(data)

    @allure.title(""""
           Scenario: Create an order
          Given the user is authenticated
          When the user creates an order with invalid details (shipDate is not a timestamp string)
          Then the system will be failed to crete order details
          And it will raise an error""")
    def test_create_pet_with_invalid_data_ship_date_is_not_time_stamp(self):
        with open('TestCase/create_order/test_data/invalid_ship_date.json', 'r') as file:
            data = json.load(file)
            store = Store()
            with pytest.raises(ValueError, match="Incorrect type for key: shipDate. Expected to be the timestamp string"):
                store.create_order(data)

    @allure.title(""""
             Scenario: Create an order
            Given the user is authenticated
            When the user creates an order with valid details but petId does not exist
            Then the system will be failed to crete order details
            And it will return 404 code""")
    def test_create_pet_with_non_exist_pet_id(self):
        with open('TestCase/create_order/test_data/non_exist_pet_id.json', 'r') as file:
            data = json.load(file)
            pet = Pet()
            resp = pet.find_pet_by_id(data['petId'])
            assert resp['status_code'] == 404


