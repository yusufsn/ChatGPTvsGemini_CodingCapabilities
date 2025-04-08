import json

# Given JSON data
sampleJson = {"id": 1, "name": "value2", "age": 29}

# Sort JSON keys alphabetically and convert to a string
sorted_json = json.dumps(sampleJson, indent=2, sort_keys=True)

# Write the sorted JSON to a file
with open('sorted_json.json', 'w') as json_file:
    json_file.write(sorted_json)

# Optional: Print the sorted JSON to the console for verification
print(sorted_json)
