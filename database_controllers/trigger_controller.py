import pymongo
import os
from database.conn import client
from database_models.models import Report
from utilities.time_converter import convert_time_to_utc
from datetime import datetime, timedelta
import uuid
# database controllers import
from database_controllers.bq_controller import get_timezone
from database_controllers.menu_controller import get_all_menu_hour
db = client['loop']
timezones = db['bq']
menus_hours = db['menu-hours']
store_status = db['store-status']
current_time = os.getenv('CURRENT_DATE_TIME')
# current_time = '2023-01-21 18:13:22.47922 UTC'
current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S.%f %Z")

reports = db['reports']



def generate_random_id():
    return str(uuid.uuid4())

def parse_time_from_string(time_string):
    # Parse the time string into a time object
    return datetime.strptime(time_string, "%H:%M:%S").time()


def get_time_ranges(store_id , timezone):
    res = get_all_menu_hour(store_id)
    start_time_ranges = [0,0,0,0,0,0,0]
    end_time_ranges = [0,0,0,0,0,0,0]

    for x in res:
        start_time_ranges[x['day']] = str(convert_time_to_utc(x['start_time_local'] , timezone))
        end_time_ranges[x['day']] = str(convert_time_to_utc(x['end_time_local'] , timezone))

    return [start_time_ranges , end_time_ranges]

def get_uptime_last_hour(store_id, start_time_range , end_time_range ):
    one_hour_ago = current_time - timedelta(hours=1)
    
    # Get the day of the week (Monday=0, Sunday=6)
    day_of_week = one_hour_ago.weekday()

    # Extract the start and end time for the current day from the dictionary
    start_time_obj = parse_time_from_string(start_time_range[day_of_week])
    end_time_obj = parse_time_from_string(end_time_range[day_of_week])

    # Combine the date from one hour ago with the extracted times to get datetime objects
    start_datetime = datetime.combine(one_hour_ago.date(), start_time_obj)
    end_datetime = datetime.combine(one_hour_ago.date(), end_time_obj)
    # print(start_datetime , end_datetime)
    low = start_datetime.strftime("%Y-%m-%d %H:%M:%S.%f") + " UTC"
    high = end_datetime.strftime("%Y-%m-%d %H:%M:%S.%f") + " UTC"
    query = {
        "store_id": store_id,
        "timestamp_utc": {
            "$gte": high,
            "$lte": low
        },
        "status":"active"
    }


    result = store_status.find(query)

    return list(result) 

def get_uptime_last_day(store_id , start_time_range , end_time_range):
    # timezone = get_timezone(store_id)
    one_day_ago = current_time - timedelta(days=1)

    # Get the day of the week (Monday=0, Sunday=6)
    day_of_week = one_day_ago.weekday()

    # Extract the start and end time for the previous day from the dictionary
    start_time_obj = parse_time_from_string(start_time_range[day_of_week])
    end_time_obj = parse_time_from_string(end_time_range[day_of_week])


    # Combine the date from one day ago with the extracted times to get datetime objects
    start_datetime = datetime.combine(one_day_ago.date(), start_time_obj)
    end_datetime = datetime.combine(one_day_ago.date(), end_time_obj)

    low = start_datetime.strftime("%Y-%m-%d %H:%M:%S.%f") + " UTC"
    high = end_datetime.strftime("%Y-%m-%d %H:%M:%S.%f") + " UTC"
    # print(low , high)
    query = {
        "store_id": store_id,
        "timestamp_utc": {
            "$gte": high ,
            "$lte": low
        },
        "status":"active"
    }


    result = store_status.find(query)

    return list(result) 

def get_uptime_last_week(store_id , start_time_range , end_time_range):
    # timezone = get_timezone(store_id)
    # Calculate the datetime for one hour ago
    one_week_ago = current_time - timedelta(weeks=1)

    # Get the day of the week (Monday=0, Sunday=6) for one week ago
    day_of_week = one_week_ago.weekday()

    # Create an empty list to store the results for each day within the week
    results = []

    # Iterate over each day of the week
    for day_of_week in range(7):
        # Extract the start and end time for the day of the week from the dictionary
        start_time_obj = parse_time_from_string(start_time_range[day_of_week])
        end_time_obj = parse_time_from_string(end_time_range[day_of_week])
        # print(start_time_obj , end_time_obj)
        # Combine the date from one week ago with the extracted times to get datetime objects
        start_datetime = datetime.combine(current_time - timedelta(days=day_of_week), start_time_obj)
        end_datetime = datetime.combine(current_time - timedelta(days=day_of_week), end_time_obj)
        
        low = start_datetime.strftime("%Y-%m-%d %H:%M:%S.%f") + " UTC"
        high = end_datetime.strftime("%Y-%m-%d %H:%M:%S.%f") + " UTC"
        # print(low , high)
        # Construct the query with the time range condition for the current day of the week
        query = {
            "store_id": store_id,
            "timestamp_utc": {
                "$gte": high,
                "$lte": low
            },
            "status":"active"
        }

        # Execute the query and get the result for the current day
        result = store_status.find(query)

        # Append the result to the list of results
        results.append(list(result))

    return results

    

def get_downtime_last_hour(store_id , start_time_range , end_time_range):
    one_hour_ago = current_time - timedelta(hours=1)
    
    # Get the day of the week (Monday=0, Sunday=6)
    day_of_week = one_hour_ago.weekday()

    # Extract the start and end time for the current day from the dictionary
    start_time_obj = parse_time_from_string(start_time_range[day_of_week])
    end_time_obj = parse_time_from_string(end_time_range[day_of_week])

    # Combine the date from one hour ago with the extracted times to get datetime objects
    start_datetime = datetime.combine(one_hour_ago.date(), start_time_obj)
    end_datetime = datetime.combine(one_hour_ago.date(), end_time_obj)
    # print(start_datetime , end_datetime)
    low = start_datetime.strftime("%Y-%m-%d %H:%M:%S.%f") + " UTC"
    high = end_datetime.strftime("%Y-%m-%d %H:%M:%S.%f") + " UTC"
    query = {
        "store_id": store_id,
        "timestamp_utc": {
            "$gte": high,
            "$lte": low
        },
        "status":"inactive"
    }


    result = store_status.find(query)

    return list(result) 

def get_downtime_last_day(store_id , start_time_range , end_time_range):
    # timezone = get_timezone(store_id)
    one_day_ago = current_time - timedelta(days=1)

    # Get the day of the week (Monday=0, Sunday=6)
    day_of_week = one_day_ago.weekday()

    # Extract the start and end time for the previous day from the dictionary
    start_time_obj = parse_time_from_string(start_time_range[day_of_week])
    end_time_obj = parse_time_from_string(end_time_range[day_of_week])


    # Combine the date from one day ago with the extracted times to get datetime objects
    start_datetime = datetime.combine(one_day_ago.date(), start_time_obj)
    end_datetime = datetime.combine(one_day_ago.date(), end_time_obj)

    low = start_datetime.strftime("%Y-%m-%d %H:%M:%S.%f") + " UTC"
    high = end_datetime.strftime("%Y-%m-%d %H:%M:%S.%f") + " UTC"
    # print(low , high)
    query = {
        "store_id": store_id,
        "timestamp_utc": {
            "$gte": high ,
            "$lte": low
        },
        "status":"inactive"
    }


    result = store_status.find(query)

    return list(result) 

def get_downtime_last_week(store_id , start_time_range , end_time_range):
    # timezone = get_timezone(store_id)
    # Calculate the datetime for one hour ago
    one_week_ago = current_time - timedelta(weeks=1)

    # Get the day of the week (Monday=0, Sunday=6) for one week ago
    day_of_week = one_week_ago.weekday()

    # Create an empty list to store the results for each day within the week
    results = []

    # Iterate over each day of the week
    for day_of_week in range(7):
        # Extract the start and end time for the day of the week from the dictionary
        start_time_obj = parse_time_from_string(start_time_range[day_of_week])
        end_time_obj = parse_time_from_string(end_time_range[day_of_week])
        # print(start_time_obj , end_time_obj)
        # Combine the date from one week ago with the extracted times to get datetime objects
        start_datetime = datetime.combine(current_time - timedelta(days=day_of_week), start_time_obj)
        end_datetime = datetime.combine(current_time - timedelta(days=day_of_week), end_time_obj)
        
        low = start_datetime.strftime("%Y-%m-%d %H:%M:%S.%f") + " UTC"
        high = end_datetime.strftime("%Y-%m-%d %H:%M:%S.%f") + " UTC"
        # print(low , high)
        # Construct the query with the time range condition for the current day of the week
        query = {
            "store_id": store_id,
            "timestamp_utc": {
                "$gte": high,
                "$lte": low
            },
            "status":"inactive"
        }

        # Execute the query and get the result for the current day
        result = store_status.find(query)

        # Append the result to the list of results
        results.append(list(result))

    return results

def trigger(store_id):
    report = Report()
    timezone = get_timezone(store_id)
    start_time_range, end_time_range = get_time_ranges(store_id , timezone['timezone_str'])
    report.uptime_last_hour = get_uptime_last_hour(store_id , start_time_range ,end_time_range)
    report.uptime_last_day = get_uptime_last_day(store_id , start_time_range , end_time_range)
    report.uptime_last_week = get_uptime_last_week(store_id , start_time_range , end_time_range)
    report.downtime_last_hour = get_downtime_last_hour(store_id , start_time_range , end_time_range)
    report.downtime_last_day = get_downtime_last_day(store_id, start_time_range , end_time_range)
    report.downtime_last_week = get_downtime_last_week(store_id , start_time_range , end_time_range)
    
    report_id = generate_random_id()
    reports.insert_one({
        "report_id":report_id,
        "uptime_last_hour" : report.uptime_last_hour,
        "uptime_last_day" : report.uptime_last_day,
        "uptime_last_week" : report.uptime_last_week,
        "downtime_last_hour" : report.downtime_last_hour,
        "downtime_last_day":report.downtime_last_day,
        "downtime_last_week":report.downtime_last_week

    })
    return report_id
