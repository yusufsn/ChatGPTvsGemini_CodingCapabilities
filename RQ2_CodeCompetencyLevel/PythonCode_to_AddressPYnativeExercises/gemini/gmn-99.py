sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Get the value for the 'city' key
city_value = sample_dict.pop('city')

# Add the 'location' key with the city value
sample_dict['location'] = city_value

print(sample_dict)
