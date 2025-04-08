import json

# JSON data (string format)
json_data = '''
[ 
  { 
    "id": 1,
    "name": "name1",
    "color": [ 
      "red",
      "green"
    ]
  },
  { 
    "id": 2,
    "name": "name2",
    "color": [ 
      "pink",
      "yellow"
    ]
  }
]
'''

# Parse the JSON data
data = json.loads(json_data)

# Extract all the 'name' values
name_values = [item['name'] for item in data]

# Print the result
print(name_values)
