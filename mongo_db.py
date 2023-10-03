import json

from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://upa:upa@cluster0.cq5pjvs.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

database_name = "upa"  # Change to your desired database name
# Change to your desired collection name
collection_name = "records"

# Load the JSON data
with open("zastupitelstvo.json", "r") as json_file:
    data = json.load(json_file)

# Connect to MongoDB
db = client[database_name]
collection = db[collection_name]

# Insert each document into the MongoDB collection
for document in data["data"]:
    collection.insert_one(document)

# Close the MongoDB connection
client.close()

print("Data inserted into MongoDB successfully.")
