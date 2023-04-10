from scripts.utilities.MySQLUtils import DBUtils
import requests
from scripts.constants import app_constants
import json


def extract_weather_forecast(raw_forecasts, station_id):
    forecasts = []
    for raw_forecast in raw_forecasts:
        forecast = []
        forecast.append(raw_forecast['dt'])
        temp = raw_forecast['main']['feels_like']
        weather = raw_forecast['weather'][0]['main']

        forecast.append(temp)
        forecast.append(weather)
        forecast.append(station_id)
        forecasts.append(forecast)
    return forecasts


def insert_weather_forecast(station_id, position):
    lat = position['lat']
    lng = position['lng']
    # weather_forecast_response = requests.get(app_constants.DataSource.WEATHER_FORECAST_API.format(lat=lat, lon=lng,
    #                                                                                               weather_api_key=app_constants.DataSource.WEATHER_API_KEY))
    # weather_forecast_data = weather_forecast_response.text
    # weather_forecast_dict = json.loads(weather_forecast_data)

    # dummy forecast:
    weather_forecast_dict = {
        "cod": "200",
        "message": 0,
        "cnt": 3,
        "list": [
            {
                "dt": 1599760800,
                "main": {
                    "temp": 66.09,
                    "feels_like": 61.48,
                    "temp_min": 64.67,
                    "temp_max": 66.09,
                    "pressure": 1021,
                    "sea_level": 1020,
                    "grnd_level": 1017,
                    "humidity": 44,
                    "temp_kf": 0.79
                },
                "weather": [
                    {
                        "id": 802,
                        "main": "Clouds",
                        "description": "多云",
                        "icon": "03d"
                    }
                ],
                "clouds": {
                    "all": 37
                },
                "wind": {
                    "speed": 5.53,
                    "deg": 314,
                    "gust": 8.3
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "d"
                },
                "dt_txt": "2020-09-10 18:00:00"
            },
            {
                "dt": 1599771600,
                "main": {
                    "temp": 61.43,
                    "feels_like": 57.49,
                    "temp_min": 59.77,
                    "temp_max": 61.43,
                    "pressure": 1021,
                    "sea_level": 1021,
                    "grnd_level": 1018,
                    "humidity": 54,
                    "temp_kf": 0.92
                },
                "weather": [
                    {
                        "id": 801,
                        "main": "Clouds",
                        "description": "晴，少云",
                        "icon": "02n"
                    }
                ],
                "clouds": {
                    "all": 22
                },
                "wind": {
                    "speed": 4.76,
                    "deg": 15,
                    "gust": 5.3
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-09-10 21:00:00"
            },
            {
                "dt": 1599782400,
                "main": {
                    "temp": 59.18,
                    "feels_like": 56.8,
                    "temp_min": 58.62,
                    "temp_max": 59.18,
                    "pressure": 1019,
                    "sea_level": 1019,
                    "grnd_level": 1016,
                    "humidity": 57,
                    "temp_kf": 0.31
                },
                "weather": [
                    {
                        "id": 802,
                        "main": "Clouds",
                        "description": "多云",
                        "icon": "03n"
                    }
                ],
                "clouds": {
                    "all": 46
                },
                "wind": {
                    "speed": 1.74,
                    "deg": 106,
                    "gust": 5.3
                },
                "visibility": 10000,
                "pop": 0,
                "sys": {
                    "pod": "n"
                },
                "dt_txt": "2020-09-11 00:00:00"
            }
        ],
        "city": {
            "id": 2643743,
            "name": "London",
            "coord": {
                "lat": 51.5085,
                "lon": -0.1257
            },
            "country": "GB",
            "population": 1000000,
            "timezone": 3600,
            "sunrise": 1599715685,
            "sunset": 1599762420
        }
    }
    weather_five_day_forecast = weather_forecast_dict['list']
    # query to flush the data @Aarya

    weather_forecast_values = extract_weather_forecast(weather_five_day_forecast, station_id)
    query = "INSERT INTO `dublinbikes`.`weather_forecast` (`predict_date`,`weather`," \
            "`temperature`,`station_id`) VALUES (%s,%s,%s,%s); "
    DBUtils().insert_multiple_rows(query, weather_forecast_values)


def get_weather_forecast_from_db(station_id, prediction_time):
    query = "SELECT * FROM `dublinbikes`.`weather_forecast` WHERE `station_id` = %s"
    prediction_rows = DBUtils().get_station_data(query, station_id)
    for predictions in prediction_rows:
        # logic to compare with given time and available time and return the best value
        pass
    # return best value
    return None
