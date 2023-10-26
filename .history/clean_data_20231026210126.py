import json

# Load the JSON data
with open("zastupitelstvo.json", "r") as json_file:
    data_json = json.load(json_file)

cleaned_data = []
for data in data_json["data"]:
    cleaned_data.append(data)
    
# Save to a file
with open('zastupitelstvo_cleaned.json', 'w') as outfile:
    json.dump(cleaned_data, outfile, indent=4)
