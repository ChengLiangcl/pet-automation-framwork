from util.request import Request

class User:
    def __init__(self): 
        self.prefix= '/user'
        self.request = Request()

    def create_user(self, payload):
        #Check payload data type
        required_fields = {
            'id': int,
            'username': str,
            'firstName': str,
            'lastName': str,
            'email': str,
            'password': str,
            'phone': str,
            'userStatus': int
        }
        for field, expected_type in required_fields.items():
            if field not in payload:
                return 400, f"Missing required field: {field} Bad Request"
            if not isinstance(payload[field], expected_type):
                return 400, f"Field '{field}' should be of type {expected_type.__name__} Bad Request!"
        code, data, message = self.request.post_request( self.prefix, payload) 
        return code, data, message
    def update_user(self, payload, username):
        
        url = f'{self.prefix}/{username}'
        code, data, message = self.request.put_request(url, payload) 
        return code, data, message
    def get_user_by_user_name(self, username):
        url = f'{self.prefix}/{username}'
        code, data, message = self.request.get_request(url)
        return code, data, message
    
    def delete_user(self,username):
        url = f'{self.prefix}/{username}'
        code, data, message = self.request.delete_request(url)
        return code, data, message
    
    def login(self, username, password):
        url = f'{self.prefix}/login?username={username}&password={password}'
        code, data, message = self.request.get_request(url)
        return code, data, message
    def logout(self):
        url = f'{self.prefix}/logout'
        code, data, message = self.request.get_request(url)
        return code, data, message
    
    def create_user_with_array(self, payload):
        url = f'{self.prefix}/createWithArray'
        code, data, message = self.request.post_request(url, payload) 
        return code, data, message

    def create_user_with_list(self, payload):
        url = f'{self.prefix}/createWithList'
        code, data, message = self.request.post_request(url, payload) 
        return code, data, message
