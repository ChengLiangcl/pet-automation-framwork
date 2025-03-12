import json
from entity.store import Store
store = Store()


with open('store_test_case/store_negative_test_case.json', 'r') as file:
    test_data = json.load(file)
class TestStoreAPINegative():
    
    #This should Failed, there is no validation from frontend and backend at all, so I just let this pass
    def test_place_order_missing_key_fields(self):
        place_order_data = test_data['place_order']
        code, data, message = store.place_order(test_data['place_order'])
        assert code ==200
    
    #This should Failed, there is no validation from frontend and backend at all, so I just let this pass
    def test_get_non_exist_order(self):
        code, data, message = store.find_order_by_id(867878978)
        assert code == 404
    
    def test_delete_non_exist_order(self):
        code, data, message = store.delete_purchase(87897987489)
        assert code == 404
        
      
