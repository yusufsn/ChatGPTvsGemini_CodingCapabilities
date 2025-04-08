# Given dictionary
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

# Get all values from the dictionary and remove duplicates by converting to a set
unique_values = list(set(speed.values()))

# Output the list of unique values
print(unique_values)
