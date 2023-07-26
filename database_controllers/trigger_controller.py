import pymongo
from database.conn import client
from database_models.models import Report
from utilities.time_converter import convert_time_to_utc

db = client['loop']

def get_uptime_last_hour(store_id):
    return 'Done'

def trigger(store_id):
    report = Report()
    report.uptime_last_hour = get_uptime_last_hour(store_id)
    return 'Done'

print(convert_time_to_utc("00:10:00" , "Asia/Beirut"))