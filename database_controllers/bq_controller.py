import pymongo
from database.conn import client
from database_models.models import Bq
db = client['loop']

bqs = db['bq']

def get_timezone(store_id):
    data = bqs.find_one({'store_id':store_id})

    if data is None:
        bq = Bq(store_id , 'America/Chicago')
        # print(bq.res())
        return bq.res()
        # return 'done'

    return data