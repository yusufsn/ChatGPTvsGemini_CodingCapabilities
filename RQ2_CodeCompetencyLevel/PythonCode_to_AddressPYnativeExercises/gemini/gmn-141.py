import json

sampleJson = {"key1": "value1", "key2": "value2"}

# Pretty-print the JSON data with custom formatting
pretty_json = json.dumps(sampleJson, indent=2, separators=(",", "="))

print(pretty_json)
