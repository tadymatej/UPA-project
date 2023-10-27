import json
from datetime import datetime, timedelta
import os

from influxdb_client_3 import InfluxDBClient3, Point

token = "VHvj7OSCceMdybeuh9V3rYbjnCrC4ZYa1wql-8HTz8Kb50LNueyDXTMcKaKez6vaGP3wu_GSqaiPhworLoa2qQ=="
org = "UPA"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = InfluxDBClient3(host=host, token=token, org=org)
database = "UPA"

script_dir = os.path.dirname(__file__)

# Read JSON data from the file
with open(script_dir + '/data/Kvalita_ovzdusi.geojson', 'r') as file:
    json_data = json.load(file)

# Extract and format the data for InfluxDB
features = json_data.get('features', [])

influx_data = []

for feature in features:
    properties = feature.get('properties', {})

    if properties:
        actualized_str = properties.get('actualized', '')
        try:
            no2_1h = properties.get('no2_1h')
            no2_1h_value = float(no2_1h) if no2_1h is not None else None
            actualized_date = datetime.fromisoformat(actualized_str[:-1])
            actualized_date = actualized_date + timedelta(days=60)
            if (datetime.now() - actualized_date) > timedelta(days=25):
                continue
            data_point = {
                'measurement': 'data_ovzdusi2',  # Update with your measurement name
                'tags': {
                    'code': properties.get('code', ''),
                    'name': properties.get('name', ''),
                },
                'time': actualized_date.isoformat(),
                'fields': {
                    'no2_1h': float(properties.get('no2_1h')) if properties.get('no2_1h') is not None else None,
                    'pm10_1h': float(properties.get('pm10_1h')) if properties.get('pm10_1h') is not None else None,
                    'pm10_24h': float(properties.get('pm10_24h')) if properties.get('pm10_24h') is not None else None,
                    'pm2_5_1h': float(properties.get('pm2_5_1h')) if properties.get('pm2_5_1h') is not None else None,
                },
            }

            influx_data.append(data_point)
        except ValueError:
            pass
for point in influx_data:
    client.write(database=database, record=point)
# Write the data to InfluxDB

# Close the InfluxDB client
client.close()
