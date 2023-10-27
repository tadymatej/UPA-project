
class JsonGeometryPoint():
    def __init__(self, pointJson) -> None:
        self.x = pointJson[0]
        self.y = pointJson[1]
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def toJson(self):
        return "[{}, {}]".format(self.x, self.y)

    def getString(self):
        return "{}{}".format(str(self.x).replace(".", ""), str(self.y).replace(".", ""))

    def print(self):
        print("x, y = [{}, {}]".format(self.x, self.y))