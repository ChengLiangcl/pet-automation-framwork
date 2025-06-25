import requests

class Request:
    def __init__(self): 
        self.prefix = "https://petstore.swagger.io/v2"
        self.headers = {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*', 
        }
        

    def get_request(self, url, payload=None):
        """
        Sends a GET request to the specified URL, prefixed by a base URL, and returns the status code and JSON response data.

        Args:
            url (str): The endpoint to append to the base URL and send the GET request to.

        Returns:
            tuple: A tuple containing the status code (int) and the JSON response data (dict).
        """
        url = self.prefix + url
        if payload:
            response = requests.get(url, params=payload)  
        else:
            response = requests.get(url)  
        status_code = response.status_code
        data = None
        if status_code!=404:
            data = response.json() 
        
        message = response.text  

        return status_code, data, message
    
    def post_request(self, url, payload, over_write_header=None):
        """
        Sends a POST request to the specified URL, prefixed by a base URL, and returns the status code and JSON response data.

        Args:
            url (str): The endpoint to append to the base URL and send the POST request to.
            payload (dict): The dictionary of data to send in the body of the POST request.

        Returns:
            tuple: A tuple containing the status code (int) and the JSON response data (dict).
        """
        url = self.prefix + url
        if (over_write_header != None):
            self.headers =  over_write_header

        response = requests.post(url, json=payload, headers=self.headers)


        message = response.text
        status_code = response.status_code
        data = None
        if status_code!=404 or status_code!=415:
            data = response.json()
        #Set Back to default 
        self.headers = {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*', 
        }

        return status_code, data, message
    

    def delete_request(self, url):
        """
        Sends a DELETE request to the specified URL, prefixed by a base URL, and returns the status code and JSON response data.

        Args:
            url (str): The endpoint to append to the base URL and send the DELETE request to.

        Returns:
            tuple: A tuple containing the status code (int) and the response data (str, dict).
        """
        url = self.prefix + url
        response = requests.delete(url, headers=self.headers)
        
        # Get the status code
        status_code = response.status_code
        message = response.text  # The raw response text
        data = None
        if status_code!=404:
            data = response.json()
        return status_code, data, message

    
    def put_request(self, url, payload):
        """
        Sends a PUT request to the specified URL, prefixed by a base URL, and returns the status code and JSON response data.

        Args:
            url (str): The endpoint to append to the base URL and send the PUT request to.
            payload (dict): The dictionary of data to send in the body of the PUT request.

        Returns:
            tuple: A tuple containing the status code (int) and the JSON response data (dict).
        """
        url = self.prefix + url

        response = requests.put(url, json=payload, headers=self.headers)
        status_code = response.status_code
        data = None
        if status_code !=404:
            data = response.json()
        message = response.text
        return status_code, data, message

        


