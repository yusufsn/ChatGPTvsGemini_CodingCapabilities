import json

# The given JSON string (incorrect version)
invalid_json = '''{
  "company": {
    "employee": {
      "name": "emma",
      "payble": {
        "salary": 7000
        "bonus": 800
      }
    }
  }
}'''

# Try to load the JSON and check if it's valid
try:
    # Attempt to parse the JSON
    data = json.loads(invalid_json)
    print("The JSON is valid.")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
    # Correct the invalid JSON
    corrected_json = '''{
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
    print("The corrected JSON is:")
    print(corrected_json)
