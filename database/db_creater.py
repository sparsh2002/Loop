import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import certifi
ca = certifi.where()
load_dotenv()
uri = os.getenv('MONGO_URI')
db = os.getenv('DB_NAME')

# MongoDB connection details
mongodb_uri = uri  # Replace with your MongoDB URI
database_name = db # Replace with your desired database name
collection_name = 'bq'  # Replace with your desired collection name

# CSV file details
csv_file_path = 'bq-results-20230125-202210-1674678181880.csv'  # Replace with the path to your CSV file

# Function to import CSV data to MongoDB
def import_csv_to_mongodb(csv_file, db_uri, db_name, collection_name):
    # Read CSV into a pandas DataFrame
    print('Started')
    df = pd.read_csv(csv_file)
    
    # Convert DataFrame records to a list of dictionaries
    data = df.to_dict(orient='records')
    
    # Connect to MongoDB
    client = MongoClient(uri, server_api=ServerApi('1'),tlsCAFile=ca)
    
    # Access the database
    db = client[db_name]
    
    # Access or create the collection
    collection = db[collection_name]
    
    # Insert data into the collection
    collection.insert_many(data)
    
    # Close the MongoDB connection
    client.close()
    print('Finished')

# Call the function to import data from CSV to MongoDB
import_csv_to_mongodb(csv_file_path, mongodb_uri, database_name, collection_name)
