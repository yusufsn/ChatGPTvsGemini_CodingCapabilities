sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]

# Remove keys from the dictionary using a loop
for key in keys:
    if key in sample_dict:
        del sample_dict[key]

print(sample_dict)
