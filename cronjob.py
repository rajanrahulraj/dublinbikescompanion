import json

import requests
import datetime
import schedule
import time

from scripts.constants import app_constants
from scripts.utilities.MySQLUtils import DBUtils


def get_weather_info(position):
    lat = position['lat']
    lng = position['lng']
    weather_response = requests.get(app_constants.DataSource.WEATHER_API.format(lat=lat, lon=lng, weather_api_key=app_constants.DataSource.WEATHER_API_KEY))
    weather_data = weather_response.text
    weather_dict = json.loads(weather_data)
    current_weather = weather_dict['weather'][0]
    current_temp = weather_dict['main']
    current_weather.update(current_temp)
    return json.dumps(current_weather)

def getStationData(data_dict):
    station_data = []
    for station in data_dict:
        station_values = []
        station_values.append(station['number'])
        station_values.append(station['banking'])
        station_values.append(station['bonus'])
        station_values.append(station['bike_stands'])
        station_values.append(station['available_bike_stands'])
        station_values.append(station['available_bikes'])
        station_values.append(station['status'])
        station_values.append(station['last_update'])
        weather = get_weather_info(station['position'])
        station_values.append(weather)
        station_data.append(station_values)

    return station_data

def fetch_data():
    try:
        response = requests.get(app_constants.DataSource.DYNAMIC_DATA_API)
        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            station_data = getStationData(data_dict)

            query = "INSERT INTO `dublinbikes`.`apidata` (`number`,`banking`," \
                    "`bonus`,`bike_stands`,`available_bike_stands`,`available_bikes`,`status`,`last_update`,`weather`, " \
                    "`data_fetch_time`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW()); "
            DBUtils().insert_multiple_rows(query, station_data)
    except Exception as e:
        print(e)


fetch_data()
# schedule.every(5).minutes.do(fetch_data)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
