import json

sampleJson = """{
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

# Parse the JSON string into a Python object
data = json.loads(sampleJson)

# Access the nested key 'salary'
salary = data['company']['employee']['payble']['salary']

# Print the salary value
print(salary)
