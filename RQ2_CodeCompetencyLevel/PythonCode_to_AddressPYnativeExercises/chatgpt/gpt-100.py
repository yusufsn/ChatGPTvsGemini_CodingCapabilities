# Given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Rename the key 'city' to 'location'
sample_dict["location"] = sample_dict.pop("city")

# Output the updated dictionary
print(sample_dict)

# Given dictionary
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

# Find the key with the minimum value
min_key = min(sample_dict, key=sample_dict.get)

# Output the key
print(min_key)
