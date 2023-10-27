
from neo4j import GraphDatabase

class Neo4jDB():
    def __init__(self, uri="neo4j+ssc://", host = "localhost", port = 7474, user = "", password = "") -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.uri = uri

    def connect(self):
        self.driver = GraphDatabase.driver(self.uri + self.host + ":" + str(self.port), auth=(self.user, self.password))

    def disconnect(self):
        self.driver.close()

    def addNode(self, label, props):
        query = "CREATE (node:{} {})".format(label, props)
        self.driver.session().run(query)