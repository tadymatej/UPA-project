import json

# Load the JSON data
with open("zastupitelstvo_debug.json", "r") as json_file:
    data_json = json.load(json_file)

final_data = {
    "last_update": "",
    "data": {}
}

cleaned_data = []
for data in data_json["data"]:
    cleaned_data.append(data)
    
final_data["last_update"] = data_json["last_update"]
final_data["data"] = cleaned_data

# Save to a file
with open('zastupitelstvo_cleaned.json', 'w') as outfile:
    json.dump(final_data, outfile, indent=4)
