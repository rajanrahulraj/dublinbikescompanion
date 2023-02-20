import json

import requests
import datetime
import schedule
import time


from scripts.constants import app_constants


def fetch_data():
    response = requests.get(app_constants.DataSource.DYNAMIC_DATA_API)
    if response.status_code == 200:
        data = response.text
        # TO-DO: Remove the sample code to insert into db instead of writing to file
        with open(f"../../data/api_data_{datetime.datetime.now().timestamp()}", "w") as f:
            f.write(data)
        data_dict = json.loads(data)
        print(data_dict)


schedule.every(1).minutes.do(fetch_data)

while True:
    schedule.run_pending()
    time.sleep(1)
