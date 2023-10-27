## Neo4j

Databáze běží přes docker

### Postup spuštění:

1) Instalujte si docker (https://docs.docker.com/desktop/install)
2) provedte následující příkaz:
    docker pull neo4j
3) Spustte následující příkaz:
    docker run \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    --env=NEO4J_AUTH=none \
    --env NEO4J_PLUGINS='["graph-data-science"]' \
    neo4j:latest

Nyní by měla běžet lokálně neo4j databáze, přístupná přes: http://localhost:7474


Script: Najdi nejvíc vytíženou trasu z bodu A do bodu B (o víkendu):
bod A: 	[16.583119100000033,49.18363480000005]
bod B: 	[16.56432250000006,49.19261460000007]


CALL gds.graph.project('myGraph', 'Point', 'spoj_rok2016');
CALL gds.graph.use('myGraph');
MATCH (start{startPoint:[16.583119100000033,49.18363480000005]}), (end{startPoint:[16.56432250000006,49.19261460000007]})
CALL gds.shortestPath.dijkstra.write.estimate('neo4j', {
    sourceNode: start,
    targetNode: end,
    relationshipWeightProperty: 'week_2016',
    writeRelationshipType: 'spoj_rok2016'
})
YIELD nodeCount, relationshipCount, bytesMin, bytesMax, requiredMemory
RETURN nodeCount, relationshipCount, bytesMin, bytesMax, requiredMemory