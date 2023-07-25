import pymongo
from database.conn import client

db = client['loop']
stores = db['store-status']

menus = db['menu-hours']

def get_store_status(store_id):
    store = stores.find_one({'store_id':store_id})
    if store is None:
        return f'Store with id {store_id} not found'
    return store

def get_all_menu_hour(store_id):
    data = menus.find({'store_id':store_id})
    res = [x for x in data]
    if len(res)==0:
        return 'store with id {store_id} is open 24x7'
    return res