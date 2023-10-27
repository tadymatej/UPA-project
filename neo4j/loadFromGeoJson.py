import json

import os


from jsonFeature import JsonFeature
from neo4jDB import Neo4jDB

script_dir = os.path.dirname(__file__)

jsonFile = open(script_dir + "/../Intenzita_dopravy.geojson", "r")
jsonData = json.load(jsonFile)
jsonFile.close()

features = jsonData["features"]

featureObjects : list[JsonFeature] = []
for item in features:
    featureObjects.append(JsonFeature(item))


db = Neo4jDB()
db.connect()

for featureObject in featureObjects:
    geometry = featureObject.getGeometry()
    db.addNode("", geometry.toJson())

db.disconnect()