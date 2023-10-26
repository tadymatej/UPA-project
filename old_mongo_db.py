import json
from datetime import datetime, timezone
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

# ALERT! For testing purpuses delete all data
#result= collection.delete_many({})

# Insert each document into the MongoDB collection
for document in data["data"]:
    date_format = "%Y-%m-%dT%H:%M:%S%z"
    parsed_datetime = datetime.strptime(document["datetime"], date_format)
    document["datetime"] = parsed_datetime
    
    # Checking if the document already exists in the database
    duplicate_document = collection.find_one({'code': document["code"], 'subject': document["subject"]})
    if duplicate_document:
        time = duplicate_document["datetime"].replace(tzinfo=timezone.utc)
        if time < parsed_datetime:
            # New document contains updated data; old document is updated
            collection.update_one({'code': document["code"], 'subject': document["subject"]}, {"$set": document}, upsert=False)
    else:
        # The document does not yet exist in the database; it is inserted into the database
        collection.insert_one(document)
        
    #collection.update_one({'code': document["code"], 'subject': document["subject"], 'datetime': {"$lt": parsed_datetime}}, {"$set": document},upsert=True)

# Close the MongoDB connection
client.close()

print("Data inserted into MongoDB successfully.")
