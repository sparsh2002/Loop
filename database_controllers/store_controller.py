import pymongo
from database.conn import client

db = client['loop']
stores = db['store-status']

def get_store_status(store_id):
    store = stores.find_one({'store_id':store_id})
    if store is None:
        return f'Store with id {store_id} not found'
    return store