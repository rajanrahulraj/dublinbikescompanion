import requests
import datetime

from scripts.constants import app_constants


def fetch_data():
    response = requests.get(app_constants.DataSource.DYNAMIC_DATA_API)
    if response.status_code == 200:
        data = response.text
        with open(f"../../data/api_data_{datetime.datetime.now().timestamp()}", "w") as f:
            f.write(data)


fetch_data()
