import pytest
import allure
from Models.store import Store


@pytest.mark.run(order=22)
class TestDeleteOrder:
    @allure.title(""""
   Scenario: Successfully delete an existing order
    Given a logged-in admin user
    And an order id does exist in the database
    When the admin sends a DELETE request to delete the record
    Then the response status code should be 200
    And order should be removed from the database
    """)
    def test_delete_order_with_existing_order_id(self):
        store = Store()
        resp = store.delete_order(10)
        status_code = resp['status_code']
        assert status_code == 200

    @allure.title(""""
    Scenario: Successfully delete an non-existing order
     Given a logged-in admin user
     And an order id does not exist in the database
     When the admin sends a DELETE request to delete the record
     Then the response status code should be 404
     And order should stay in the database
     """)
    def test_delete_order_with_non_existing_order_id(self):
        store = Store()
        resp = store.delete_order(46421215456)
        status_code = resp['status_code']
        data = resp['data']
        assert status_code == 404
        assert data['message'] == "Order Not Found"
