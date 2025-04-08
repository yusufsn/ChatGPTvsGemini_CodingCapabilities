# Given list and dictionary
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

# Iterate through the list and remove elements that are not in the dictionary values
roll_number = [num for num in roll_number if num in sample_dict.values()]

# Output the modified list
print("After removing unwanted elements from list", roll_number)
