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
## QUERIES - Aggregation
# 1. Jake navrhy ze schuze s kodem Z9/09 byly prijaty?
print("1. Jake navrhy ze schuze s kodem Z9/09 byly prijaty?")
code = "Z9/09"
result = "Přijato"
agg_result1 = collection.aggregate(
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
agg_result2 = collection.aggregate([
        {"$match": {"code": code, "result": result}},
        {"$group": {"_id": "$code", "accepted_total": {"$sum": 1}}}
    ])

for ar2 in agg_result2:
    print("\t>>", ar2)

## QUARIES - MapReduce
# !ALERT! MapReduce was removed from pymongo 4.0. MapReduce operations can be rewritten using aggregation pipeline operators, such as $group, $merge, and others.
# Src: https://pymongo.readthedocs.io/en/stable/migrate-to-pymongo4.html#collection-map-reduce-and-collection-inline-map-reduce-are-removed
#      https://www.mongodb.com/docs/manual/reference/map-reduce-to-aggregation-pipeline/

# 3. Kdo se v hlasovani o navrhu bodu: "162. Návrh Prohlášení k rozdělení práva k nemovité věci na vlastnické právo k jednotkám k pozemku p. č. 40, jehož součástí je budova č. p. 643, stavba občanského vybavení, to vše v k. ú. Město Brno"
#    zdrzel hlasovani? ("abstained")
print("3. Kdo se v hlasovani o navrhu bodu: 162. Návrh Prohlášení k rozdělení práva k nemovité věci na vlastnické právo k jednotkám k pozemku p. č. 40, jehož součástí je budova č. p. 643, stavba občanského vybavení, to vše v k. ú. Město Brno zdrzel hlasovani?")
subject = "162. Návrh Prohlášení k rozdělení práva k nemovité věci na vlastnické právo k jednotkám k pozemku p. č. 40, jehož součástí je budova č. p. 643, stavba občanského vybavení, to vše v k. ú. Město Brno"
option = "Zdržel se"
agg_result3 = collection.aggregate([
    {"$match": {"subject": subject}},
    {"$unwind": {"path": "$parties"}},
    {"$unwind": {"path": "$parties.votes"}},
    {"$match": {"parties.votes.option": option}},
    {"$group": {"_id": "$parties.votes.voter"}},
])
for ar3 in agg_result3:
    print("\t>>", ar3)

# 4. U kolika hlasování byl každý zastupitel nepřítomen?
print("4. U kolika hlasování byl každý zastupitel nepřítomen?")
option=None
text="nepřít."
agg_result4 = collection.aggregate([
    {"$unwind": {"path": "$parties"}},
    {"$unwind": {"path": "$parties.votes"}},
    {"$group": {"_id": "$parties.votes.voter", "absence": {"$sum": {"$cond": [{"$and": [{"$eq":["$parties.votes.option", option]}, {"$eq":["$parties.votes.text", text]}]}, 1, 0]}}}}
])
for ar4 in agg_result4:
    print("\t>>", ar4)
