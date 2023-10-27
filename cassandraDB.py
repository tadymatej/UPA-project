from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Your JSON data
json_data = {
    "type": "FeatureCollection",
    "name": "firmy_firmy",
    # ... (the rest of your JSON)
}

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



cloud_config = {
    'secure_connect_bundle': 'secure-connect-upa.zip'
}
auth_provider = PlainTextAuthProvider(username='user', password='pass')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

# Connect to the Cassandra cluster
# cluster = Cluster(['localhost'])  # Replace with your Cassandra cluster address

# # Create a session and keyspace
# session = cluster.connect()
session.execute(
    "CREATE KEYSPACE IF NOT EXISTS my_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}")
session.execute("USE my_keyspace")

# Create a table to store the properties
session.execute("""
    CREATE TABLE IF NOT EXISTS properties (
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
        globalid UUID
    )
""")

# Insert the extracted properties into the Cassandra table
for properties in properties_data:
    insert_query = """
        INSERT INTO properties (
            objectid, name, adresa, foundation_year, employees, turnover_in_czk,
            website, odvetvi, industry, address, city, latitude, longitude, globalid
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    session.execute(insert_query, (
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
    ))

# Close the Cassandra session and cluster connection
session.shutdown()
cluster.shutdown()
