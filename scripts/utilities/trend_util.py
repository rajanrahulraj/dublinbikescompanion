import datetime

from scripts.utilities.MySQLUtils import DBUtils
from statistics import mean


def get_weekly_trend_from_db(station_id, current_time):

    #Add the time difference 1 - 7 days to the current time and add it into a days datetime list
    #In the days datetime list take a one hour time period and fetch the data that comes from it.
    #If only one of the data comes up, directly take that value. If more comes up take the average.
    #Send a dictionary with 7 timestamps as key and includes available bikes and available stands


    # #Justs for testing remove in production @Aarya:
    # time_period = datetime.timedelta(weeks=4)
    # current_time = current_time - time_period


    historic_data_dict = dict()
    for day_before in range(1,8):
        time_period_day = datetime.timedelta(days=day_before)
        data_fetch_day = current_time - time_period_day
        time_period_half_hour = datetime.timedelta(minutes=30)

        data_fetch_start_time = current_time - time_period_half_hour
        data_fetch_end_time = current_time + time_period_half_hour

        query = "SELECT `available_bikes`,`available_bike_stands`,`data_fetch_time` FROM `dublinbikes`.`apidata` WHERE `number` = " \
                "%s and `data_fetch_time` > %s and `data_fetch_time` < %s"
        historic_data_rows = DBUtils().get_station_data_with_time(query, station_id, data_fetch_start_time,
                                                                  data_fetch_end_time)

        available_bikes_list = []
        available_stands_list = []
        for historic_data in historic_data_rows:
            available_bikes, available_stands, data_fetch_time = historic_data
            available_bikes_list.append(available_bikes)
            available_stands_list.append(available_stands)


        data_fetch_time_ts = int(round(data_fetch_day.timestamp()))
        data_fetch_time_str = str(data_fetch_time_ts)
        historic_data_dict[data_fetch_time_str] = {"bikes_available_avg":int(mean(available_bikes_list)), "stands_available_avg":int(mean(available_stands_list))}

    return historic_data_dict


def get_today_hourly_data_from_db(station_id, current_time):
    #From the current time get the threshold by replacing the hour and minute to the time 12 AM
    #Get all the data which is greater than this time
    #Put it in a dictionary of time against the bike availability and send it back

    # # Justs for testing remove in production @Aarya:
    # time_period = datetime.timedelta(weeks=4)
    # current_time = current_time - time_period

    current_time_day_start = current_time.replace(hour=0,minute=0)

    query = "SELECT `available_bikes`,`available_bike_stands`,`data_fetch_time` FROM `dublinbikes`.`apidata` WHERE " \
            "`number` = " \
            "%s and `data_fetch_time` > %s"
    historic_data_rows = DBUtils().get_station_data_with_time_threshold(query, station_id, current_time_day_start)

    historic_data_dict = dict()
    for historic_data in historic_data_rows:
        available_bikes, available_stands, data_fetch_time = historic_data
        data_fetch_time_ts = int(round(data_fetch_time.timestamp()))
        data_fetch_time_str = str(data_fetch_time_ts)
        historic_data_dict[data_fetch_time_str] = {"bikes_available_avg": available_bikes,
                                                   "stands_available_avg": available_stands}

    return historic_data_dict







