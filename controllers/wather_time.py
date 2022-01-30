import json
from flask import jsonify


class WatherTime:
    def __init__(self):
        whater_data = [
            {
                "date": "1/1/20",
                "was_rainy": False
            },
            {
                "date": "1/2/20",
                "was_rainy": True
            },
            {
                "date": "1/3/20",
                "was_rainy": True
            },
            {
                "date": "1/4/20",
                "was_rainy": False
            },
            {
                "date": "1/5/20",
                "was_rainy": False
            },
            {
                "date": "1/6/20",
                "was_rainy": True
            },
            {
                "date": "1/7/20",
                "was_rainy": False
            },
            {
                "date": "1/8/20",
                "was_rainy": True
            },
            {
                "date": "1/9/20",
                "was_rainy": True
            },
            {
                "date": "1/10/20",
                "was_rainy": True
            }
        ]
        self.whater_data = whater_data

    def listDays(self):
        result = []
        for(index, value) in enumerate(self.whater_data[:-1]):
            actual, next = value, self.whater_data[index+1]
            if (actual['was_rainy'] == False and next['was_rainy'] == True):
                result.append(next)
        return jsonify({
            'error': False,
            'success': True,
            'data': result
        })
