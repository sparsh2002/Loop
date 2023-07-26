from flask import Flask, request
from database import decoder
from database import conn
from database import decoder
# imports from database controllers
from database_controllers.store_controller import get_store_status 
from database_controllers.menu_controller import get_all_menu_hour , get_menu_hour_for_day
from database_controllers.bq_controller import get_timezone

# import utilities
from utilities.time_converter import convert_time_to_utc

# Create a Flask app instance
app = Flask(__name__)
app.json_encoder = decoder.MongoJSONEncoder

# Route for the homepage
@app.route('/')
def home():
    return 'Hello, welcome to my Flask app!'

# Route for another page
@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/database/store-status/<int:store_id>' , methods = ['GET' , 'POST'])
def store_status(store_id):
    if request.method == 'GET':
        res = get_store_status(store_id)
        return res

@app.route('/database/menu-hours/<int:store_id>', methods=['GET'])
def menu_hours(store_id):
    if request.method=='GET':
        if request.args.get('day') is not None:
            res = get_menu_hour_for_day(store_id , int(request.args.get('day')))
            return res
        else:
            res = get_all_menu_hour(store_id)
            return res
    else:
        return 'Method not defined'
    
@app.route('/database/timezones/<int:store_id>', methods=['GET'])
def timezones(store_id):
    if request.method=='GET':
        print('Hello')
        res = get_timezone(store_id)
        return res
    else:
        return 'Method not defined'


if __name__ == '__main__':
    # Run the app in debug mode on http://127.0.0.1:5000/
    app.run(debug=True)
