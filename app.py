from flask import Flask
from database import decoder
from database import conn
# Create a Flask app instance
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return 'Hello, welcome to my Flask app!'

# Route for another page
@app.route('/about')
def about():
    return 'This is the about page.'

if __name__ == '__main__':
    # Run the app in debug mode on http://127.0.0.1:5000/
    app.run(debug=True)
