import json

json_data = """{
"company":{
"employee":{
"name":"emma",
"payble":{
"salary":7000,
"bonus":800
}
}
}
}"""

try:
    json.loads(json_data)
    print("JSON is valid")
except json.JSONDecodeError as e:
    print("JSON is invalid:", e)
    # Correct the missing comma after "salary":7000
    corrected_json = """{
    "company":{
    "employee":{
    "name":"emma",
    "payble":{
    "salary":7000,
    "bonus":800
    }
    }
    }
    }"""
    print("Corrected JSON:")
    print(corrected_json)
