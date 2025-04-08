import json

json_data = """
[
{
"id":1,
"name":"name1",
"color":[
"red",
"green"
]
},
{
"id":2,
"name":"name2",
"color":[
"pink",
"yellow"
]
}
]
"""

# Parse the JSON data
data = json.loads(json_data)

# Extract names from the list of dictionaries
names = [item['name'] for item in data]

print(names)
