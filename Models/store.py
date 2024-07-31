import re
import sys
import os

import requests

path = sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Models.request import *


class Store:
    @staticmethod
    def get_inventory():
        resp = get_method(f'https://petstore.swagger.io/v2/store/inventory')
        return resp

    @staticmethod
    def get_order_by_order_id(id):
        resp = get_method(f"https://petstore.swagger.io/v2/store/order/{id}")
        return resp

    @staticmethod
    def create_order(order_info):
        Store.validate_data(order_info)
        resp = post_method("https://petstore.swagger.io/v2/store/order", order_info)
        return resp

    @staticmethod
    def validate_data(data):
        required_keys = {
            "id": int,
            "petId": int,
            "quantity": int,
            "shipDate": str,
            "status": str,
            "complete": bool
        }
        for key, expected_type in required_keys.items():
            if key not in data:
                raise ValueError(f"Missing key: {key}")

            if not isinstance(data[key], expected_type):
                raise ValueError(f"Incorrect type for key: {key}. Expected {expected_type}, got {type(data[key])}")
        regx = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$'
        if not re.match(regx, data['shipDate']):
            raise ValueError("Incorrect type for key: shipDate. Expected to be the timestamp string")

    @staticmethod
    def delete_order(order_id):
        api = f'https://petstore.swagger.io/v2/store/order/{order_id}'
        response = delete_method(api)
        return response

