import json
from entity.user import User
user = User()

with open('user_test_case/negative_case_test_data.json', 'r') as file:
    test_data = json.load(file)
def test_delete_user_not_exist():
    code, data, message = user.delete_user('none-exist')
    assert code == 404

def test_get_user_does_not_exist():
    code, data, message = user.get_user_by_user_name('none-exist')
    assert code ==404
    
def test_create_user_missing_id_field():
    payload = test_data['test_create_user_missing_id_field']
    code, message = user.create_user(payload)
    assert code == 400
    assert message == 'Missing required field: id Bad Request'

    


    
    
    