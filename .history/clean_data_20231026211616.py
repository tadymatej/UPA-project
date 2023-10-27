import json

# Load the JSON data
with open("zastupitelstvo.json", "r") as json_file:
    data_json = json.load(json_file)

final_data = {
    "last_update": "",
    "data": []
}

for data in data_json["data"]:
    final_data["data"].append(data)
    
final_data["last_update"] = data_json["last_update"]

# Save to a file
with open('zastupitelstvo_cleaned.json', 'w',  encoding='utf-8') as outfile:
    json.dump(final_data, outfile, indent=4, ensure_ascii=False)
