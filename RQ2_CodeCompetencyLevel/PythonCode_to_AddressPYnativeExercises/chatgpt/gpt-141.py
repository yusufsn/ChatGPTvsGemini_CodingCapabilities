import json

# Given JSON data
sampleJson = {"key1": "value1", "key2": "value2"}

# Pretty-print JSON with indent level 2 and custom separators
pretty_json = json.dumps(sampleJson, indent=2, separators=(',', ' = '))

# Print the pretty-printed JSON
print(pretty_json)
