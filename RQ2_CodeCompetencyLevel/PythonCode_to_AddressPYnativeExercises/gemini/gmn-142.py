import json

sampleJson = {"id": 1, "name": "value2", "age": 29}

# Sort the JSON keys alphabetically
sorted_json = {k: sampleJson[k] for k in sorted(sampleJson.keys())}

# Write the sorted JSON to a file
with open("sorted_json.json", "w") as f:
    json.dump(sorted_json, f, indent=2)
