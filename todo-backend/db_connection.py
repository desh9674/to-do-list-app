from pymongo import MongoClient
import os

# Load MongoDB URI from environment variable or hardcode it
MONGODB_URI = os.getenv("MONGODB_URI")
print(MONGODB_URI)
#mongodb+srv://jennie:1234@mainuseastmern.pdigz2c.mongodb.net/?retryWrites=true&w=majority&appName=mainuseastMern&ssl=false

# Connect to MongoDB
client = MongoClient(MONGODB_URI)
try:
    print("connected to the db")
    print(client.list_database_names())
except Exception as e:
    print("erroed out while connecting to db")
    print(e)
db = client["testing1"]  # Connect to the 'testing1' database

# Access the collection
tasks_collection = db["tasks"]  # Define the collection for tasks
