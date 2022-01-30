import json
from flask import jsonify


class CostumeOrders:
    def __init__(self):
        orders = [
            {
                "order_number": "ORD_1567",
                "item_name": "LAPTOP",
                "status": "SHIPPED"
            },
            {
                "order_number": "ORD_1567",
                "item_name": "MOUSE",
                "status": "SHIPPED"
            },
            {
                "order_number": "ORD_1567",
                "item_name": "KEYBOARD",
                "status": "PENDING"
            },
            {
                "order_number": "ORD_1234",
                "item_name": "GAME",
                "status": "SHIPPED"
            },
            {
                "order_number": "ORD_1234",
                "item_name": "BOOK",
                "status": "CANCELLED"
            },
            {
                "order_number": "ORD_1234",
                "item_name": "BOOK",
                "status": "CANCELLED"
            },
            {
                "order_number": "ORD_9834",
                "item_name": "PANTS",
                "status": "CANCELLED"
            },
            {
                "order_number": "ORD_9834",
                "item_name": "SHIRT",
                "status": "SHIPPED"
            },
            {
                "order_number": "ORD_7654",
                "item_name": "TV",
                "status": "CANCELLED"
            },
            {
                "order_number": "ORD_7654",
                "item_name": "DVD",
                "status": "CANCELLED"
            },
                    
        ]
        self.orders = orders

    def listOrders(self):
        result = []
        alReadySearch=[]
        for value in self.orders:
            identifier = value['order_number']
            if not identifier in alReadySearch:
                resultFilter = list(filter(lambda val: val['order_number'] == identifier, self.orders))
                if any(d['status'] == 'PENDING' for d in resultFilter):
                    result.append({'order_number': identifier, 'status': 'PENDING'})
                elif all(val['status'] == 'CANCELLED' for val in resultFilter):
                    result.append({'order_number': identifier, 'status': 'CANCELLED'})
                else:
                    result.append({'order_number': identifier, 'status': 'SHIPPED'})
                alReadySearch.append(identifier)
        return jsonify({
            'error': False,
            'success': True,
            'data': result
        })
