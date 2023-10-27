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
    neo4j

Nyní by měla běžet lokálně neo4j databáze, přístupná přes: http://localhost:7474
