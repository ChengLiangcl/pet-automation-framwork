import requests


# Implement the get method avoid the same api request for calling multiple time
def get_method(api):
    headers = {
        'Accept': 'application/json'
    }
    # Make the GET request
    response = requests.get(api, headers=headers)
    print(response.status_code)
    return response.json()


# Implement the post method avoid the same api request for calling multiple time

def post_method(api, test_data):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post(api, json=test_data, headers=headers)
    return response.json()


# Implement the delete method avoid the same api request for calling multiple time
def delete_method(username):
    url = f"https://petstore.swagger.io/v2/user/{username}"
    headers = {
        "accept": "application/json",
    }
    response = requests.delete(url, headers=headers)
    return response.status_code


# Implement the put method avoid the same api request for calling multiple time
def put_method(api, test_data):
    # Define the headers
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.put(api, json=test_data, headers=headers)
    return response.json()
