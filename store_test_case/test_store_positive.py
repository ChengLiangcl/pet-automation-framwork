import json
from entity.store import Store
store = Store()


with open('store_test_case/store_positive_test_data.json', 'r') as file:
    test_data = json.load(file)
class TestStoreAPIPositive():
    def test_get_inventory(self):
        code, data, message = store.get_inventory()
        assert code == 200
    
    def test_place_order(self):
        place_order_data = test_data['place_order']
        code, data, message = store.place_order(test_data['place_order'])
        assert code ==200
        assert data['id'] == place_order_data['id']
        assert data["petId"] == place_order_data['petId']
        assert data["quantity"] == place_order_data['quantity']
        assert data["complete"] == place_order_data['complete']
    
    def test_get_order(self):
        code, data, message = store.find_order_by_id(9)
        place_order_data = test_data['place_order']
        assert code == 200
        assert data['id'] == place_order_data['id']
        assert data["petId"] == place_order_data['petId']
        assert data["quantity"] == place_order_data['quantity']
        assert data["complete"] == place_order_data['complete']
    
    def test_delete_order(self):
        code, data, message = store.delete_purchase(9)
        assert code == 200
        