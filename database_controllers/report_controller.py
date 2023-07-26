import pymongo
import os
from database.conn import client
db = client['loop']
reports = db['reports']

def get_report_by_id(report_id):
    report = reports.find_one({'report_id':report_id})
    if report is None:
        return f'Report with id {report_id} not found'
    return report