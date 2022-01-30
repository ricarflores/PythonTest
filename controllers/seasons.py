import json
from flask import jsonify
import datetime
class Seasons:
    def __init__(self):
        season_orders = [
            {
                "ORD_ID": 1,
                "ORD_DT": "9/23/19",
                "QT_ORDD": 1
            },
            {
                "ORD_ID": 2,
                "ORD_DT": "1/1/20",
                "QT_ORDD": 1
            },
            {
                "ORD_ID": 3,
                "ORD_DT": "12/5/19",
                "QT_ORDD": 1
            },
            {
                "ORD_ID": 4,
                "ORD_DT": "9/24/20",
                "QT_ORDD": 1
            },
            {
                "ORD_ID": 5,
                "ORD_DT": "1/30/20",
                "QT_ORDD": 1
            },
            {
                "ORD_ID": 6,
                "ORD_DT": "5/2/20",
                "QT_ORDD": 1
            },
            {
                "ORD_ID": 7,
                "ORD_DT": "4/2/20",
                "QT_ORDD": 1
            },
            {
                "ORD_ID": 8,
                "ORD_DT": "10/9/20",
                "QT_ORDD": 1
            }
        ]
        self.season_orders = season_orders

    def seasonData(self):
        result = []
        for value in self.season_orders:
            date = value['ORD_DT']
            stringToDate = datetime.datetime.strptime(date, "%m/%d/%y")
            season = self.getSeasonPerDate(self,stringToDate,stringToDate.year)
            value['season'] = season
            result.append({
                'ORD_ID': value['ORD_ID'],
                'SEASON': season,
            })
        return jsonify({
            'error': False,
            'success': True,
            'data': result
        })
        
        

    @staticmethod
    def getSeasonPerDate(self, date, year):
        try:
            #spring = {'dayInit': '19', 'montInit': '3', 'dayEnd': '19', 'monthEnd':'6'}
            #summer = {'dayInit': '20', 'montInit': '6', 'dayEnd': '21', 'monthEnd':'9'}
            #fall = {'dayInit': '22', 'montInit': '9', 'dayEnd': '20', 'monthEnd':'12'}
            #winter = {'dayInit': '20', 'montInit': '12', 'dayEnd': '18', 'monthEnd':'3'}
            springInit = datetime.datetime(year, 3, 19)
            springEnd = datetime.datetime(year, 6, 19)
            summerInit = datetime.datetime(year, 6,20)
            summerEnd = datetime.datetime(year, 9,21)
            fallInit= datetime.datetime(year, 9,22)
            fallEnd = datetime.datetime(year, 12, 20)
            winterInit = datetime.datetime(year, 12, 20)
            winterEnd = datetime.datetime(year+1, 3, 18)
            #print(date)
            #print(year)
            #print("Sprint Interval : %a - %b ", springInit, springEnd)
            #print("Summer Interval : %a - %b ", summerInit, summerEnd)
            #print("Fall Interval : %a - %b ",fallInit, fallEnd)
            #print("Winter Interval : %a - %b ", winterInit, winterEnd)
            if springInit <= date <= springEnd:
                return "Spring"
            elif summerInit <= date <= summerEnd:
                return "Summer"
            elif fallInit <= date <= fallEnd:
                return "Fall"
            else:
                return "Winter"
        except Exception as err:
            print(err)
            return "ErrorProcess"