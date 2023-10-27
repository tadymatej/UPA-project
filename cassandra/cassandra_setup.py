import json
import os

import pandas as pd
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster

script_dir = os.path.dirname(__file__)

ASTRA_DB_APPLICATION_TOKEN = ""
ASTRA_TOKEN_PATH = script_dir + '/data/UPA-token4.json'
with open(ASTRA_TOKEN_PATH, "r") as f:
    creds = json.load(f)
    ASTRA_DB_APPLICATION_TOKEN = creds["token"]

data = pd.read_csv(
    script_dir + '/data/Obsazenost_parkovacich_domu_a_parkovist___Car_parks_capacity_data_-_live.csv')

cluster = Cluster(cloud={
    "secure_connect_bundle": script_dir + "/data/secure-connect-upa.zip",
},
auth_provider=PlainTextAuthProvider(
    "token",
    ASTRA_DB_APPLICATION_TOKEN,
),)
session = cluster.connect("bamboo")

session.execute("USE bamboo")

# Create a table to store the properties
session.execute("""
    CREATE TABLE IF NOT EXISTS parking (
        X DOUBLE,
        Y DOUBLE,
        ObjectId INT PRIMARY KEY,
        name TEXT,
        capacity INT,
        free INT,
        Latitude DOUBLE,
        Longitude DOUBLE,
        spacesSubscribersVacant INT,
        spacesSubscribersOccupied INT,
        spacesAllUsersVacant INT,
        spacesAllUsersOccupied INT,
        cars INT,
        capacity_procent DOUBLE,
        startdate TEXT,
        CapacityForPublic INT
    )
""")

# Insert the new data into the Cassandra table
for index, item in data.iterrows():
    # print(item["X"])
    insert_query = """
        INSERT INTO parking (
            X, Y, ObjectId, name, capacity, free, Latitude, Longitude,
            spacesSubscribersVacant, spacesSubscribersOccupied, spacesAllUsersVacant,
            spacesAllUsersOccupied, cars, capacity_procent, startdate, CapacityForPublic
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    session.execute(session.prepare(insert_query), [
        item["X"], item["Y"], item["ObjectId"], item["name"], item["capacity"], item["free"],
        item["Latitude"], item["Longitude"], item["spacesSubscribersVacant"], item["spacesSubscribersOccupied"],
        item["spacesAllUsersVacant"], item["spacesAllUsersOccupied"], item["cars"], item["capacity_procent"],
        item["startdate"], item["CapacityForPublic"]
    ])
# Close the Cassandra session and cluster connection
session.shutdown()
cluster.shutdown()
