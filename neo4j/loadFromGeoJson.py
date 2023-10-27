import json

import os


from jsonFeature import JsonFeature
from neo4jDB import Neo4jDB

script_dir = os.path.dirname(__file__)

jsonFile = open(script_dir + "/data/Intenzita_dopravy.geojson", "r")
jsonData = json.load(jsonFile)
jsonFile.close()

features = jsonData["features"]

featureObjects : list[JsonFeature] = []
for item in features:
    featureObjects.append(JsonFeature(item))


db = Neo4jDB()
db.connect()
db.clearDatabase()

def insertNodes(featureObjects):
    for featureObject in featureObjects:
        geometry = featureObject.getGeometry()
        points = geometry.getPoints()
        startPoint = points[0]
        endPoint = points[len(points) - 1]
        startPointJson = startPoint.toJson()
        endPointJson = endPoint.toJson() 
        startLabelNode = "ids{}".format(startPoint.getString())
        endLabelNode = "ide{}".format(endPoint.getString())
        db.addNode("Crossroad:{}".format(startLabelNode), "{" + "point: {}".format(startPointJson) + "}")
        db.addNode("Crossroad:{}".format(endLabelNode), "{" + "point: {}".format(endPointJson) + "}")

def addRelations(featureObjects, year):
    for featureObject in featureObjects:
        geometry = featureObject.getGeometry()
        points = geometry.getPoints()
        startPoint = points[0]
        endPoint = points[len(points) - 1]
        startPointJson = startPoint.toJson()
        endPointJson = endPoint.toJson() 
        startLabelNode = "ids{}".format(startPoint.getString())
        endLabelNode = "ide{}".format(endPoint.getString())
        db.addNode("Crossroad:{}".format(startLabelNode), "{" + "point: {}".format(startPointJson) + "}")
        db.addNode("Crossroad:{}".format(endLabelNode), "{" + "point: {}".format(endPointJson) + "}")
        relationJson = featureObject.getYearJson(year)
        db.softAddRelation("spoj_rok{}".format(year), startLabelNode, endLabelNode, relationJson)
        db.softAddRelation("spoj_rok{}".format(year), endLabelNode, startLabelNode, relationJson)

insertNodes(featureObjects)

addRelations(featureObjects, "2016")
addRelations(featureObjects, "2016")
addRelations(featureObjects, "2018")
addRelations(featureObjects, "2020")
addRelations(featureObjects, "2022")

startPointJson = featureObjects[0].getGeometryPoints()[0].toJson()
endPointJson = featureObjects[0].getGeometryPoints()[10].toJson()

db.shortestPathWeek("{" + "point: {}".format(startPointJson) + "}", "{" + "point: {}".format(endPointJson) + "}")

db.disconnect()