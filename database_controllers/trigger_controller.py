import pymongo
from database.conn import client
from database_models.models import Report
from utilities.time_converter import convert_time_to_utc

# database controllers import
from database_controllers.bq_controller import get_timezone

db = client['loop']
timezones = db['bq']
menus_hours = db['menu-hours']
store_status = db['store-status']


def get_uptime_last_hour(store_id):
    timezone = get_timezone(store_id)
    
    return 'Done'

def get_uptime_last_day(store_id):
    return 'Done'

def get_uptime_last_week(store_id):
    return 'Done'

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