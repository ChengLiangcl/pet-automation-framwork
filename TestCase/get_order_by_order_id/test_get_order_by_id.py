import pytest
import allure
from Models.store import Store


@pytest.mark.run(order=17)
class TestGetOrderById:
    @allure.title(""""
    Scenario: query an order by valid order_id
    Given the user is authenticated
    When the user requests an order with existing order id
    Then the system should return the order details
    """)
    def test_get_order_by_valid_id(self):
        store = Store()
        resp = store.get_order_by_order_id(10)
        user_data = resp['data']
        status_code = resp['status_code']
        assert user_data['id'] == 10
        assert status_code == 200

    @allure.title(""""
      Scenario: query an order by non-exist order_id
      Given the user is authenticated
      When the user requests an order with non-existing order id
      Then the system should return the message order not found
      """)
    def test_get_order_by_non_exist_order_id(self):
        store = Store()
        resp = store.get_order_by_order_id(100)
        user_data = resp['data']
        assert user_data['message'] == 'Order not found'
        assert resp['status_code'] == 404
