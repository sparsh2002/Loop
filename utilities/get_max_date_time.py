import pymongo
from database.conn import client
from database_models.models import Bq
db = client['loop']

store_status = db['store-status']

def get_max_date_time():
    print('started')
    pipeline = [
        {
            '$group': {
                '_id': None,
                'maxDate': {'$max': '$' + 'timestamp_utc'}
            }
        }
    ]

    result = list(store_status.aggregate(pipeline))
    print(result)
    print('Finished')
    if result:
        max_date = result[0]['maxDate']
        return max_date
    else:
        return None
