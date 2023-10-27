import json

from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster

# Your JSON data
json_data = {
    "type": "FeatureCollection",
    "name": "firmy_firmy",
    # ... (the rest of your JSON)
}

with open('Firmy_v_Brno.geojson', 'r') as file:
    json_data = json.load(file)

ASTRA_DB_APPLICATION_TOKEN = ""
ASTRA_TOKEN_PATH = 'UPA-token4.json'
with open(ASTRA_TOKEN_PATH, "r") as f:
    creds = json.load(f)
    ASTRA_DB_APPLICATION_TOKEN = creds["token"]
# Function to extract properties from the JSON


def extract_properties(data):
    properties_list = []
    features = data.get("features", [])
    for feature in features:
        properties = feature.get("properties", {})
        properties_list.append(properties)
    return properties_list


# Extract properties from the JSON
properties_data = extract_properties(json_data)


cluster = Cluster(cloud={
    "secure_connect_bundle": "/Users/janzimola/Documents/VUT/UPA-project/secure-connect-upa.zip",
},
    auth_provider=PlainTextAuthProvider(
    "token",
    ASTRA_DB_APPLICATION_TOKEN,
),)
session = cluster.connect("bamboo")

# Connect to the Cassandra cluster
# cluster = Cluster(['localhost'])  # Replace with your Cassandra cluster address

# # Create a session and keyspace
# session = cluster.connect()
# session.execute(
#     "CREATE KEYSPACE IF NOT EXISTS bamboo WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}")
session.execute("USE bamboo")

# Create a table to store the properties
session.execute("""
    CREATE TABLE IF NOT EXISTS firmy (
        objectid INT PRIMARY KEY,
        name TEXT,
        adresa TEXT,
        foundation_year INT,
        employees TEXT,
        turnover_in_czk TEXT,
        website TEXT,
        odvetvi TEXT,
        industry TEXT,
        address TEXT,
        city TEXT,
        latitude DOUBLE,
        longitude DOUBLE,
        globalid TEXT
    )
""")

# Insert the extracted properties into the Cassandra table
# print(properties_data)
for properties in properties_data:
    # print(properties)
    # print((
    #     properties.get("objectid"),
    #     properties.get("name"),
    #     properties.get("adresa"),
    #     properties.get("foundation_year"),
    #     properties.get("employees"),
    #     properties.get("turnover_in_czk"),
    #     properties.get("website"),
    #     properties.get("odvetvi"),
    #     properties.get("industry"),
    #     properties.get("address"),
    #     properties.get("city"),
    #     properties.get("latitude"),
    #     properties.get("longitude"),
    #     properties.get("globalid"),
    # ))
    # break
    insert_query = """
        INSERT INTO firmy (
            objectid, name, adresa, foundation_year, employees, turnover_in_czk,
            website, odvetvi, industry, address, city, latitude, longitude, globalid
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    session.execute(session.prepare(insert_query), [

        properties.get("objectid"),
        properties.get("name"),
        properties.get("adresa"),
        properties.get("foundation_year"),
        properties.get("employees"),
        properties.get("turnover_in_czk"),
        properties.get("website"),
        properties.get("odvetvi"),
        properties.get("industry"),
        properties.get("address"),
        properties.get("city"),
        properties.get("latitude"),
        properties.get("longitude"),
        properties.get("globalid"),
    ])

# Close the Cassandra session and cluster connection
session.shutdown()
cluster.shutdown()
