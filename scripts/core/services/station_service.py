import requests
from flask import Blueprint, jsonify

from scripts.constants import app_constants

station_service_router = Blueprint('station_service_router', __name__, url_prefix="/stations")


@station_service_router.route('/contract')
def get_stations_Contract():
    url = f'{app_constants.DataSource.DUBLIN_BIKES_BASE_API}/stations'
    params = {'contract': 'dublin', 'apiKey': f'{app_constants.DataSource.API_KEY}'}
    response = requests.get(url, params=params)
    data = response.json()
    return jsonify(data)


@station_service_router.route('/list')
def get_stations_lists():
    url = f'{app_constants.DataSource.DUBLIN_BIKES_BASE_API}/stations'
    params = {'apiKey': f'{app_constants.DataSource.API_KEY}'}
    response = requests.get(url, params=params)
    data = response.json()
    return jsonify(data)


@station_service_router.route('/19')
def get_stationInfo():
    url = f'{app_constants.DataSource.DUBLIN_BIKES_BASE_API}/stations/19'
    params = {'contract': 'rouen', 'apiKey': f'{app_constants.DataSource.API_KEY}'}
    response = requests.get(url, params=params)
    data = response.json()
    return jsonify(data)

