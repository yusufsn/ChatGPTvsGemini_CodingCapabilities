import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

# Load the JSON string into a Python dictionary
data = json.loads(sampleJson)

# Access the value of key2
key2_value = data["key2"]

# Print the value of key2
print(key2_value)
