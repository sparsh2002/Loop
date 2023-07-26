import pymongo
from database.conn import client

db = client['loop']

class Store:
    def __init__(self, store_id, status, timestamp_utc):
        self.store_id = store_id
        self.status = status
        self.timestamp_utc = timestamp_utc


class Menu:
    def __init__(self , store_id , day , start_time_local , end_time_local):
        self.store_id = store_id
        self.day = day
        self.start_time_local = start_time_local
        self.end_time_local = end_time_local


class Bq:
    def __init__(self , store_id , timezone_str):
        self.store_id = store_id
        self.timezone_str = timezone_str
    def res(self):
        data = {}
        data['store_id'] = self.store_id
        data['timezone_str'] = self.timezone_str
        return data
    
class Report:
    def __init__(self , store_id, uptime_last_hour ,
                  uptime_last_day,uptime_last_week , 
                  downtime_last_hour,downtime_last_day,
                  downtime_last_week):
        self.store_id = store_id
        self.uptime_last_hour = uptime_last_hour # minutes
        self.uptime_last_day = uptime_last_day # hours
        self.uptime_last_week = uptime_last_week # hours
        self.downtime_last_hour = downtime_last_hour
        self.downtime_last_day = downtime_last_day
        self.downtime_last_week = downtime_last_week
    def __init__(self):
        pass
    def print(self):
        print('Uptime Last Hour:' , self.uptime_last_hour)
        print('Uptime Last day:' , self.uptime_last_day )
        print('Uptime Last Week:', self.uptime_last_week)
        print('Downtime Last Hour:' , self.downtime_last_hour)
        print('Downtime Last day:' , self.downtime_last_day )
        print('Downtime Last Week:', self.downtime_last_week)

    def res(self):
        dict = {}

        dict['uptime_last_hour'] = self.uptime_last_hour
        dict['uptime_last_day'] = self.uptime_last_day
        dict['uptime_last_week'] = self.uptime_last_week
        dict['downtime_last_day'] = self.downtime_last_day
        dict['downtime_last_hour'] = self.downtime_last_hour
        dict['downtime_last_week'] = self.downtime_last_week

        return dict
