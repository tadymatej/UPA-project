import json
from datetime import datetime
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

# ALERT! For testing purpuses delete all data
#result= collection.delete_many({})

# Insert each document into the MongoDB collection
pid = vid = 1
for data in data_json["data"]:
    date_format = "%Y-%m-%dT%H:%M:%S%z"
    parsed_datetime = datetime.strptime(data["datetime"], date_format)
    data["datetime"] = parsed_datetime
    
    sid = f"{data['code']}_{data['number']}"
    print(sid)
    
    subject = {
        "_id": sid,
        "code": data["code"],
        "number": data["number"],
        "datetime": parsed_datetime,
        "subject": data["subject"],
        "result": data["result"],
        "details": data["details"]
    }
    
    subjects.update_one({"code": data["code"], "number": data["number"]}, {"$set": subject}, upsert=True)
    for p in data["parties"]:
        party = {
        "_id": pid,
        "name": p["name"],
        "details": p["details"],
        "votes": p["votes"],
        "sid": sid,
        }
        parties.update_one({"name": p["name"], "sid": sid}, {"$set": party}, upsert=True)
        
        pid+=1
    
# Close the MongoDB connection
client.close()

print("Data inserted into MongoDB successfully.")
