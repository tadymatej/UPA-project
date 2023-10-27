
from neo4j import GraphDatabase, RoutingControl

class Neo4jDB():
    def __init__(self, uri="neo4j://", host = "localhost", port = 7687, user = "", password = "") -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.uri = uri

    def connect(self, database = "neo4j"):
        self.driver = GraphDatabase.driver(self.uri + self.host + ":" + str(self.port), auth=(self.user, self.password))
        self.database = database

    def disconnect(self):
        self.driver.close()

    def _execute_query_w(self, query):
        self.driver.execute_query(query, {}, routing_=RoutingControl.WRITE, database_=self.database)

    def _execute_query_r(self, query):
        return self.driver.execute_query(query, {}, routing_=RoutingControl.READ, database_=self.database)

    def clearDatabase(self):
        query = "MATCH (n) DETACH DELETE n"
        self._execute_query_w(query)

    def addNode(self, label, props):
        if label == "":
            query = "MERGE (node" + props + ")"
        else:
            query = "MERGE (node:" + label + props + ")"
        self._execute_query_w(query)

    def getLabelFromNodeProps(self, propsJson):
        query = "MATCH(a{}) RETURN labels(a)".format(propsJson)
        return self._execute_query_r(query)

    def softAddRelation(self, name, nodeFromLabel, nodeToLabel, props):
        query = "MATCH(a:{}), (b:{}) MERGE(a)-[rel:{}]->(b) SET rel = properties({})".format(nodeFromLabel, nodeToLabel, name, props)
        self._execute_query_w(query)

    def addRelation(self, name, nodeFromLabel, nodeToLabel):
        query = "MATCH(a:{}), (b:{}) MERGE(a)-[:{}]->(b)".format(nodeFromLabel, nodeToLabel, name)
        self._execute_query_w(query)

    def prepareGraph(self, graphName, relationshipPropName):
        query = """
        CALL gds.graph.drop('""" + graphName + """', False)"""
        self._execute_query_w(query)
        
        query = """CALL gds.graph.project(
            '""" + graphName + """',
            'Crossroad',
            'spoj_rok2016',
            {
                relationshipProperties: '""" + relationshipPropName + """'
            }
        );"""
        self._execute_query_w(query)

    def shortestPathWeekend(self, sourcePointJson, targetPointJson):
        self.shortestPath(sourcePointJson, targetPointJson, 'weekend')
    
    def shortestPathWeek(self, sourcePointJson, targetPointJson):
        self.shortestPath(sourcePointJson, targetPointJson, 'week')

    def shortestPath(self, sourcePointJson, targetPointJson, relationshipPropName):
        self.prepareGraph('myGraph', relationshipPropName)
        query = """
        MATCH (source""" + sourcePointJson + """), (target""" + targetPointJson + """)
        CALL gds.shortestPath.dijkstra.stream('myGraph', {
            sourceNode: source,
            targetNode: target,
            relationshipWeightProperty: '""" + relationshipPropName + """"'
        })
        YIELD index, sourceNode, targetNode, totalCost, nodeIds, costs, path
        RETURN
            index,
            gds.util.asNode(sourceNode).name AS sourceNodeName,
            gds.util.asNode(targetNode).name AS targetNodeName,
            totalCost,
            [nodeId IN nodeIds | gds.util.asNode(nodeId).name] AS nodeNames,
            costs,
            nodes(path) as path
        ORDER BY index

        """
        return self._execute_query_r(query)