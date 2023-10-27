

import json
from jsonGeometry import JsonGeometry
from jsonGeometryPoint import JsonGeometryPoint

class JsonFeature():
    def __init__(self, featureJson) -> None:
        properties = featureJson["properties"]
        self.properties = properties
        self.ID = properties["id"]
        self.week_2016 = properties["prac_16"]
        self.weekend_2016 = properties["vik_16"]
        self.week_2018 = properties["prac_18"]
        self.weekend_2018 = properties["vik_18"]
        self.week_2020 = properties["prac_20"]
        self.weekend_2020 = properties["vik_20"]
        self.week_2022 = properties["prac_22"]
        self.weekend_2022 = properties["vik_22"]
        self.exportDate = properties["datum_exportu"]
        self.globalID = properties["GlobalID"]
        self.objectID = properties["ObjectId"]
        self.geometry = JsonGeometry(featureJson["geometry"])

    def getYearJson(self, strYear):
        jsonStr = "{"
        jsonStr += "week:" + str(self.properties["prac_" + strYear[2:]]) + ","
        jsonStr += "weekend:" + str(self.properties["vik_" + strYear[2:]])
        jsonStr += "}"
        return jsonStr

    def getID(self):
        return self.ID

    def getObjectID(self):
        return self.objectID

    def getWeek2016(self):
        return self.week_2016

    def getWeekend2016(self):
        return self.weekend_2016

    def getWeek2018(self):
        return self.week_2016

    def getWeekend2018(self):
        return self.weekend_2016

    def getWeek2020(self):
        return self.week_2016

    def getWeekend2020(self):
        return self.weekend_2016

    def getWeek2022(self):
        return self.week_2016

    def getWeekend2022(self):
        return self.weekend_2016

    def getGlobalID(self):
        return self.globalID
    
    def getGeometryPoints(self) -> list[JsonGeometryPoint]:
        return self.geometry.getPoints()

    def getGeometry(self) -> JsonGeometry:
        return self.geometry

    def print(self):
        print("ID {}".format(self.ID))
        self.geometry.print()
