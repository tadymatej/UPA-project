
from jsonGeometryPoint import JsonGeometryPoint

class JsonGeometry():
    def __init__(self, geometryJson) -> None:
        self.points : list[JsonGeometryPoint] = []

        for point in geometryJson["coordinates"][0]:
            self.points.append(JsonGeometryPoint(point))

    def getPoints(self) -> list[JsonGeometryPoint]:
        return self.points

    def toJson(self):
        json = "["
        jsonItems = []
        for point in self.getPoints():
            jsonItems.append(str(point.getX()))
            jsonItems.append(str(point.getY()))
        json += ", ".join(jsonItems)
        json += "]"
        return json

    def print(self):
        for point in self.points:
            point.print()
