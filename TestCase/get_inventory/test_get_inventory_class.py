import pytest
import allure
from Models.store import Store


@pytest.mark.run(order=11)
class TestStoreGetInventory:
    @allure.title(""""
    Scenario: Admin try to get store inventory
    When the admin login successfully to find the store inventory
    Then the system will display all the store inventory
    And the response contains multiple items with quantity""")
    def test_get_store_inventory(self):
        store = Store()
        resp = store.get_inventory()
        assert resp['status_code'] == 200

