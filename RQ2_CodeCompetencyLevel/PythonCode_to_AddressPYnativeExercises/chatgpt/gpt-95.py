# Given lists and default values
employees = ['Kelly', 'Emma']
defaults = {"designation": "Developer", "salary": 8000}

# Initialize the dictionary with default values
employee_dict = {employee: defaults.copy() for employee in employees}

# Output the resulting dictionary
print(employee_dict)
