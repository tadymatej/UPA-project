import json

# Load the JSON data
with open("zastupitelstvo_old.json", "r") as json_file:
    data_json = json.load(json_file)

final_data = {
    "last_update": "",
    "data": []
}

for data in data_json["data"]:
    if data['code'] == "" or data['number'] == "" or data['subject'] == "":
        continue

    final_data["data"].append(data)
    
final_data["last_update"] = data_json["last_update"]

# Save to a file
with open('zastupitelstvo.json', 'w',  encoding='utf-8') as outfile:
    json.dump(final_data, outfile, indent=4, ensure_ascii=False)
