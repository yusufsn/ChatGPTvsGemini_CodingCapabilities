# Given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to extract
keys = ["name", "salary"]

# Extracting the specified keys
new_dict = {key: sample_dict[key] for key in keys}

# Output the new dictionary
print(new_dict)
