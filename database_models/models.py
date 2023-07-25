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
