employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# Create a dictionary using dictionary comprehension
result_dict = {employee: defaults.copy() for employee in employees}

print(result_dict)
