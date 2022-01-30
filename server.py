from controllers.wather_time import WatherTime
from controllers.seasons import Seasons
from controllers.costume_order import CostumeOrders
from flask import request, jsonify
import flask
app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/wather/time', methods=['GET'])
def getWatherTime():
    try:
        days = WatherTime()
        res = days.listDays()
    except Exception as err:
        print(err)
        res = jsonify({
            'error': True,
            'success': False,
            'data': []
        })
    finally:
        return res

@app.route('/season/ordes', methods=['GET'])
def getOrdersSeason():
    try:
        seasons = Seasons()
        res = seasons.seasonData()
    except Exception as err:
        print(err)
        res = jsonify({
            'error': True,
            'success': False,
            'data': "Error Proces"
        })
    finally:
        return res

@app.route('/costume/ordes', methods=['GET'])
def getCostumeOrders():
    try:
        orders = CostumeOrders()
        res = orders.listOrders()
    except Exception as err:
        print(err)
        res = jsonify({
            'error': True,
            'success': False,
            'data': "Error Proces"
        })
    finally:
        return res


if __name__ == '__main__':
    app.run(port='5050')
