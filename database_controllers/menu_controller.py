import pymongo
from database.conn import client

db = client['loop']

menus = db['menu-hours']
def get_all_menu_hour(store_id):
    data = menus.find({'store_id':store_id})
    res = [x for x in data]
    if len(res)==0:
        return 'store with id {store_id} is open 24x7'
    return res

def get_menu_hour_for_day(store_id , day):
    data = menus.find_one({'store_id':store_id , 'day':day})

    if data is None:
        return 'store with id {store_id} is open 24x7'
    
    return data