sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

# Access the nested dictionary for 'emp3'
emp3_dict = sample_dict['emp3']

# Update the 'salary' key within the 'emp3' dictionary
emp3_dict['salary'] = 8500

print(sample_dict)
