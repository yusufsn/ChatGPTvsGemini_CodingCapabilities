sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]

# Create a new dictionary using dictionary comprehension
new_dict = {key: sample_dict[key] for key in keys}

print(new_dict)
