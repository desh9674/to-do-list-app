from pymongo import MongoClient
import os

from dotenv import load_dotenv
load_dotenv()


# Load MongoDB URI from environment variable
MONGODB_URI = os.getenv("MONGODB_URI")
if not MONGODB_URI:
    raise ValueError("No MongoDB URI found in environment variables.")

# Connect to MongoDB
try:
    client = MongoClient(MONGODB_URI)
    print("Connected to the db")
    print(client.list_database_names())
except Exception as e:
    print(f"Database connection failed: {e}")
    raise e

db = client["testing1"]  # Connect to the 'testing1' database

# Access the collection
tasks_collection = db["tasks"]  # Define the collection for tasks
