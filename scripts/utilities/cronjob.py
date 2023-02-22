import json

import requests
import datetime
import schedule
import time


from scripts.constants import app_constants
from scripts.utilities.MySQLUtils import DBUtils


def fetch_data():
    try:
        response = requests.get(app_constants.DataSource.DYNAMIC_DATA_API)
        if response.status_code == 200:
            data = response.text
            data_dict = json.loads(data)
            query = "INSERT INTO `dublinbikes`.`apidata` (`number`,`contract_name`,`name`,`address`,`position`,`banking`," \
                    "`bonus`,`bike_stands`,`available_bike_stands`,`available_bikes`,`status`,`last_update`, " \
                    "`data_fetch_time`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW()); "
            values = [list(val.values()) for val in data_dict]
            for val in values:
                for index in range(len(val)):
                    if type(val[index]) == dict:
                        val[index] = json.dumps(val[index])
            DBUtils().insert_multiple_rows(query, values)
    except Exception as e:
        print(e)


# fetch_data()
schedule.every(2).minutes.do(fetch_data)

while True:
    schedule.run_pending()
    time.sleep(1)
