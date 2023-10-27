from datetime import datetime, timedelta

from influxdb_client import InfluxDBClient, Point, WritePrecision

token = "VHvj7OSCceMdybeuh9V3rYbjnCrC4ZYa1wql-8HTz8Kb50LNueyDXTMcKaKez6vaGP3wu_GSqaiPhworLoa2qQ=="
org = "UPA"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = InfluxDBClient(host=host, token=token, org=org)
database = "UPA"

query = """
SELECT *
FROM "your_measurement_name"
WHERE
time >= now() - interval '30 day' AND time <= now()
"""


# Execute the query
table = client.query(query=query, database="UPA", language='sql')

# Convert to dataframe
df = table.to_pandas().sort_values(by="time")
print(df)
