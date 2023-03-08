from flask import Flask
from flask_restful import Api
from flask import jsonify
import requests

app = Flask(__name__)
api = Api(app)

@app.route('/stations/contract')
def get_stations_Contract():
    url = 'https://api.jcdecaux.com/vls/v1/stations'
    params = {'contract': 'dublin', 'apiKey': '345d8f2cc1b7c5cf1bd07cbea465c9b0ee666e6a'}
    response = requests.get(url, params=params)
    data = response.json()
    return jsonify(data)

@app.route('/stationslist')
def get_stations_lists():
    url = 'https://api.jcdecaux.com/vls/v1/stations'
    params = {'apiKey': '345d8f2cc1b7c5cf1bd07cbea465c9b0ee666e6a'}
    response = requests.get(url, params=params)
    data = response.json()
    return jsonify(data)

@app.route('/contractslist')
def get_contracts():
    url = 'https://api.jcdecaux.com/vls/v1/contracts'
    params = {'apiKey': '345d8f2cc1b7c5cf1bd07cbea465c9b0ee666e6a'}
    response = requests.get(url, params=params)
    data = response.json()
    return jsonify(data)

@app.route('/stations/19')
def get_stationInfo():
    url = 'https://api.jcdecaux.com/vls/v1/stations/19'
    params = {'contract': 'rouen', 'apiKey': '345d8f2cc1b7c5cf1bd07cbea465c9b0ee666e6a'}
    response = requests.get(url, params=params)
    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)