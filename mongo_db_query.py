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
collection = db[collection_name]

###############################################################################
## QUERIES
# 1. Vyber prijate navrhy z hlasovani s kodem Z9/09
print("1. Jake navrhy z hlasovani s kodem Z9/09 byly prijaty?")
code = "Z9/09"
result = "Přijato"
agg_result1 = collection.aggregate(
    [{
        "$match": {"code": code, "result": result}
    }]
    )

for ar1 in agg_result1:
    print("\t>>", ar1["subject"])
    
# 2. Kolik navrhu z hlasovani s kodem Z9/09 bylo prijato? A jaka?
print("2. Kolik navrhu z hlasovani s kodem Z9/09 bylo prijato?")
code = "Z9/09"
result = "Přijato"
agg_result2 = collection.aggregate([
        {"$match": {"code": code, "result": result}},
        {"$group": {"_id": "$code", "accepted_total": {"$sum": 1}}}
    ])

for ar2 in agg_result2:
    print("\t>>", ar2)

# 3. Kdo se v hlasovani o navrhu bodu: "162. Návrh Prohlášení k rozdělení práva k nemovité věci na vlastnické právo k jednotkám k pozemku p. č. 40, jehož součástí je budova č. p. 643, stavba občanského vybavení, to vše v k. ú. Město Brno"
#    zdrzel hlasovani? ("abstained")
