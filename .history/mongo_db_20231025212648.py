import json
from datetime import datetime, timezone
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://upa:upa@cluster0.cq5pjvs.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

database_name = "upa"

# Load the JSON data
with open("zastupitelstvo.json", "r") as json_file:
    data_json = json.load(json_file)

# Connect to MongoDB
db = client[database_name]
subjects = db["subjects"]
parties = db["parties"]
votes = db["votes"]

# ALERT! For testing purpuses delete all data
#result= collection.delete_many({})

# Insert each document into the MongoDB collection
sid = pid = vid = 0
for data in data_json["data"]:
    date_format = "%Y-%m-%dT%H:%M:%S%z"
    parsed_datetime = datetime.strptime(data["datetime"], date_format)
    data["datetime"] = parsed_datetime
    
    # Checking if the navrh already exists in the database
    """duplicate_document = collection.find_one({'code': navrh["code"], 'subject': navrh["subject"]})
    if duplicate_document:
        time = duplicate_document["datetime"].replace(tzinfo=timezone.utc)
        if time < parsed_datetime:
            # New navrh contains updated data; old navrh is updated
            collection.update_one({'code': navrh["code"], 'subject': navrh["subject"]}, {"$set": navrh}, upsert=False)
    else:
        # The navrh does not yet exist in the database; it is inserted into the database
        collection.insert_one(navrh)"""
        
    subject = {
        "code": data["code"],
        "number": data["number"],
        "datetime": {"$lt": parsed_datetime},
        "subject": data["subject"],
        "result": data["result"],
        "details": data["details"]
    }
    data.update_one({"code": data["code"], "subject": data["subject"], "datetime": {"$lt": parsed_datetime},"subject":data["subject"], "result": data["result"], "details":data["details"], "pid": pid})
    subjects.update_one({"code": data["code"], "subject": data["subject"], "datetime": {"$lt": parsed_datetime},})
# Close the MongoDB connection
client.close()

print("Data inserted into MongoDB successfully.")
