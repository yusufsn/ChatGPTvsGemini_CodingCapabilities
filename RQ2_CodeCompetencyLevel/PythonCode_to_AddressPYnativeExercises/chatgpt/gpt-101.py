# Given dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

# Update Brad's salary to 8500
for key, value in sample_dict.items():
    if value['name'] == 'Brad':
        value['salary'] = 8500
        break

# Output the updated dictionary
print(sample_dict)
