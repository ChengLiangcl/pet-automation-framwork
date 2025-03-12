from util.request import Request

class Store:
    def __init__(self): 
        self.prefix= '/store'
        self.request = Request()

    def place_order(self, payload):
        url = f'{self.prefix}/order'
        code, data, message = self.request.post_request( url, payload) 
        return code, data, message
    def find_order_by_id(self, order_id):
        url = f'{self.prefix}/order/{order_id}' 
        code, data, message = self.request.get_request(url)
        return code, data, message
    
    def delete_purchase(self,order_id):
        url = f'{self.prefix}/order/{order_id}'
        code, data, message = self.request.delete_request(url)
        return code, data, message
    def get_inventory(self):
        url = f'{self.prefix}/inventory'
        code, data, message = self.request.get_request(url)
        return code, data, message

        