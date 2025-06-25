import time
import pytest
import json
from entity.user import User

# Load the test data from the JSON file
with open('user_test_case/positive_case_data.json', 'r') as file:
    test_data = json.load(file)

user = User()
payload = test_data['create_user_data']
create_user_with_list_payload= test_data['create_user_with_list']
def test_create_user():
    """Test for creating a user"""
    code, data, message = user.create_user(payload)
    assert code == 200, "Failed to create the user, please make sure all the inputs are valid"
    assert data.get('message') == str(payload['id']), "Failed to create the user"
    assert data.get('type') == 'unknown'
        
    code, data, message = user.get_user_by_user_name('jason.liang.cheng')
    assert code == 200, "Failed to find the user"
    assert data['email'] == payload['email']
    assert data['firstName'] == payload['firstName']
    assert data['username'] == payload['username']
    assert data['lastName'] == payload['lastName']
    assert data['password'] == payload['password']
    assert data['phone'] == payload['phone']


def test_update_user():
    """Test for updating a user's information"""
    copy_data = payload.copy()
    copy_data['password'] = '456465456'
    code, data, message = user.update_user(copy_data, payload['username'])
    assert code == 200, "Failed to update the user record"

    code, data, message = user.get_user_by_user_name(payload['username'])
    assert data['password'] == '456465456', "Failed to update the password"

def test_login():
    """Test for logging in the user"""
    code, data, message = user.login(payload['username'], payload['password'])
    assert code == 200, "Failed to login"

def test_log_out():
    """Test for logging out the user"""
    code, data, message = user.logout()
    assert code == 200, "Unable to logout"
def test_bulk_crate_user():
    code, data, message = user.create_user_with_list(create_user_with_list_payload)
    assert code ==200, "Failed to create multiple users"
    print(data)
    #Make sure the user can be found in the database
    code, data, message = user.get_user_by_user_name('testing.user')
    assert code ==200, "User does not exist"
    code, data, message = user.get_user_by_user_name('testing.checking')
    assert code ==200, "User does not exist"
    
    #Clean up the records 
    code, data, message = user.delete_user('testing.user')
    assert code ==200
    code,data,message = user.delete_user('testing.checking')
    assert code ==200

def test_bulk_create_user_with_array():
    code, data, message = user.create_user_with_array(create_user_with_list_payload)
    assert code ==200, "Failed to create multiple users"
        
    #Make sure the user can be found in the database
    code, data, message = user.get_user_by_user_name('testing.user')
    assert code ==200, "User does not exist"
    code, data, message = user.get_user_by_user_name('testing.checking')
    assert code ==200, "User does not exist"

    
    #Clean up the records 
    code, data, message = user.delete_user('testing.user')
    assert code ==200
    code,data,message = user.delete_user('testing.checking')
    assert code ==200
    
    
def test_delete_user():
    """Test for deleting the user"""
    code, data, message = user.delete_user(payload['username'])
    assert code == 200, "Failed to delete the user"
    
