from flask import Flask
from flask import jsonify
import requests

from scripts.core.services.station_service import station_service_router
from scripts.constants import app_constants

app = Flask(__name__)

app.register_blueprint(station_service_router)

@app.route('/stationslist')
def get_stations_lists():
    url = f'{app_constants.DataSource.DUBLIN_BIKES_BASE_API}/stations'
    params = {'apiKey': f'{app_constants.DataSource.API_KEY}'}
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