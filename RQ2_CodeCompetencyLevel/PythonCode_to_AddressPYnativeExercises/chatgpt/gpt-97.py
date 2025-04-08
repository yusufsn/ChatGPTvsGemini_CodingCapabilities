# Given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

# Removing the specified keys
for key in keys:
    sample_dict.pop(key, None)  # Using pop with default None to avoid KeyError

# Output the updated dictionary
print(sample_dict)
