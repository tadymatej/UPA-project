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
db.clearDatabase()

def insertNodes(featureObjects):
    for featureObject in featureObjects:
        geometry = featureObject.getGeometry()
        points = geometry.getPoints()
        startPoint = points[0]
        endPoint = points[len(points) - 1]
        startPointJson = startPoint.toJson()
        endPointJson = endPoint.toJson() 
        db.addNode("id" + str(featureObject.getObjectID()), "{" + "coordinates: {}, startPoint: {}, endPoint: {}".format(geometry.toJson(), startPointJson, endPointJson) + "}")

def insertRelations(featureObjects, yearStr):
    for featureObject in featureObjects:
        geometry = featureObject.getGeometry()
        points = geometry.getPoints()
        startPoint = points[0]
        endPoint = points[len(points) - 1]
        startPointJson = startPoint.toJson()
        endPointJson = endPoint.toJson() 

        startNodesLabels = db.getLabelFromNodeProps("{endPoint: " + endPointJson + "}")
        endNodesLabels = db.getLabelFromNodeProps("{startPoint: " + endPointJson + "}")

        startLabelNode = "id" + str(featureObject.getObjectID())
        for j in range(0, int(len(endNodesLabels) / 3)):
            for endLabel in endNodesLabels[j * 3]:
                endLabelNode = endLabel["labels(a)"][0]
                relationJson = featureObject.getYearJson(yearStr)
                db.softAddRelation("spoj_rok{}".format(yearStr), startLabelNode, endLabelNode, relationJson)

       #for i in range(0, int(len(startNodesLabels) / 3)):
       #     for startLabel in startNodesLabels[i * 3]:
       #         startLabelNode = startLabel["labels(a)"][0]

        #        for j in range(0, int(len(endNodesLabels) / 3)):
        #            for endLabel in endNodesLabels[j * 3]:
        #                endLabelNode = endLabel["labels(a)"][0]
        #                relationJson = featureObject.getYearJson(yearStr)
        #                db.softAddRelation("spoj_rok{}".format(yearStr), startLabelNode, endLabelNode, relationJson)

insertNodes(featureObjects)
insertNodes(featureObjects)

insertRelations(featureObjects, "2016")
insertRelations(featureObjects, "2016")
insertRelations(featureObjects, "2016")
#insertRelations(featureObjects, "2018")
#insertRelations(featureObjects, "2020")
#insertRelations(featureObjects, "2022")

db.disconnect()