import json

from pymongo import MongoClient

# Define MongoDB connection details
mongodb_host = "localhost"
mongodb_port = 27017
database_name = "your_database_name"  # Change to your desired database name
# Change to your desired collection name
collection_name = "your_collection_name"

# Load the JSON data
with open("your_json_file.json", "r") as json_file:
    data = json.load(json_file)

# Connect to MongoDB
client = MongoClient(mongodb_host, mongodb_port)
db = client[database_name]
collection = db[collection_name]

# Insert each document into the MongoDB collection
for document in data["data"]:
    collection.insert_one(document)

# Close the MongoDB connection
client.close()

print("Data inserted into MongoDB successfully.")
