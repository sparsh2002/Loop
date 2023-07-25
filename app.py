from flask import Flask, request
from database import decoder
from database import conn
from database import decoder
# imports from database controllers
from database_controllers.store_controller import get_store_status

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
        # print(res)
        return res

if __name__ == '__main__':
    # Run the app in debug mode on http://127.0.0.1:5000/
    app.run(debug=True)
