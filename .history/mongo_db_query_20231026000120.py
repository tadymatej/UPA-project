from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://upa:upa@cluster0.cq5pjvs.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

database_name = "upa"  # Change to your desired database name
# Change to your desired collection name
collection_name = "records"

# Connect to MongoDB
db = client[database_name]
subjects = db["subjects"]
parties = db["parties"]
votes = db["votes"]

###############################################################################
## QUERIES - Aggregation
# 1. Jake navrhy ze schuze s kodem Z9/09 byly prijaty?
print("1. Jake navrhy ze schuze s kodem Z9/09 byly prijaty?")
code = "Z9/09"
result = "Přijato"
agg_result1 = subjects.aggregate(
    [
        {"$match": {"code": code, "result": result}},
        {"$group": {"_id": "$subject"}}
    ])

for ar1 in agg_result1:
    print("\t>>", ar1)
    

# 2. Kolik navrhu ze schuze s kodem Z9/09 bylo prijato?
print("2. Kolik navrhu ze schuze s kodem Z9/09 bylo prijato?")
code = "Z9/09"
result = "Přijato"
agg_result2 = subjects.aggregate([
        {"$match": {"code": code, "result": result}},
        {"$group": {"_id": "$code", "accepted_total": {"$sum": 1}}}
    ])

for ar2 in agg_result2:
    print("\t>>", ar2)
