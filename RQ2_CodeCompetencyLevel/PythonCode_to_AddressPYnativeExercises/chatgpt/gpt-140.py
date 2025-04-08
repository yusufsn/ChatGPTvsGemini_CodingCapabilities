import json

# Given JSON string
sampleJson = '{"key1": "value1", "key2": "value2"}'

# Parse the JSON string into a Python dictionary
parsed_json = json.loads(sampleJson)

# Access and print the value of key2
print(parsed_json["key2"])
