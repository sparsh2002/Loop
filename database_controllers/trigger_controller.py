import pymongo
import os
from database.conn import client
from database_models.models import Report
from utilities.time_converter import convert_time_to_utc
from datetime import datetime, timedelta
# database controllers import
from database_controllers.bq_controller import get_timezone

db = client['loop']
timezones = db['bq']
menus_hours = db['menu-hours']
store_status = db['store-status']
current_time = os.getenv('CURRENT_DATE_TIME')
# current_time = '2023-01-21 18:13:22.47922 UTC'
current_time = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S.%f %Z")

def get_uptime_last_hour(store_id):
    # timezone = get_timezone(store_id)
    one_hour_ago = current_time - timedelta(hours=1)
    query = {
        "store_id": store_id,
        "timestamp_utc": {"$gte": one_hour_ago.strftime("%Y-%m-%d %H:%M:%S.%f %Z")},
        "status":"active"
    }


    result = store_status.find(query)

    return list(result) 

def get_uptime_last_day(store_id):
    # timezone = get_timezone(store_id)
    one_day_ago = current_time - timedelta(days=1)
    query = {
        "store_id": store_id,
        "timestamp_utc": {"$gte": one_day_ago.strftime("%Y-%m-%d %H:%M:%S.%f %Z")},
        "status":"active"
    }


    result = store_status.find(query)

    return list(result) 

def get_uptime_last_week(store_id):
    # timezone = get_timezone(store_id)
    # Calculate the datetime for one hour ago
    one_week_ago = current_time - timedelta(weeks=1)
    query = {
        "store_id": store_id,
        "timestamp_utc": {"$gte": one_week_ago.strftime("%Y-%m-%d %H:%M:%S.%f %Z")},
        "status":"active"
    }

    result = store_status.find(query)


    return list(result) 

def get_downtime_last_hour(store_id):
    return 'Done'

def get_downtime_last_day(store_id):
    return 'Done'

def get_downtime_last_week(store_id):
    return 'Done'

def trigger(store_id):
    report = Report()
    report.uptime_last_hour = get_uptime_last_hour(store_id)
    report.uptime_last_day = get_uptime_last_day(store_id)
    report.uptime_last_week = get_uptime_last_week(store_id)
    report.downtime_last_hour = get_downtime_last_hour(store_id)
    report.downtime_last_day = get_downtime_last_day(store_id)
    report.downtime_last_week = get_downtime_last_week(store_id)
    return report

print(convert_time_to_utc("00:10:00" , "Asia/Beirut"))