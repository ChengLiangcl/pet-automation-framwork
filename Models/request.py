import requests


# Implement the get method avoid the same api request for calling multiple time
def get_method(api):
    headers = {
        'Accept': 'application/json'
    }
    # Make the GET request
    response = requests.get(api, headers=headers)
    return {"status_code": response.status_code, "data": response.json()}


# Implement the post method avoid the same api request for calling multiple time

def post_method(api, test_data):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post(api, json=test_data, headers=headers)
    return {"status_code": response.status_code, "data": response.json()}


# Implement the delete method avoid the same api request for calling multiple time
def delete_method(api):
    url = api
    headers = {
        "accept": "application/json",
    }
    response = requests.delete(url, headers=headers)
    result = {"status_code": response.status_code}
    try:
        result["data"] = response.json()
    except ValueError:
        pass
    return result


# Implement the put method avoid the same api request for calling multiple time
def put_method(api, test_data):
    # Define the headers
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.put(api, json=test_data, headers=headers)
    return {"status_code": response.status_code, "data": response.json()}
