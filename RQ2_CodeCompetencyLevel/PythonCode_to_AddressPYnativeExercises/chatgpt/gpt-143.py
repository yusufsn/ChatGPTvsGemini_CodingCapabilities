import json

# Given JSON string
sampleJson = '''{
  "company": {
    "employee": {
      "name": "emma",
      "payble": {
        "salary": 7000,
        "bonus": 800
      }
    }
  }
}'''

# Parse the JSON string into a Python dictionary
parsed_json = json.loads(sampleJson)

# Access and print the value of salary
print(parsed_json["company"]["employee"]["payble"]["salary"])
