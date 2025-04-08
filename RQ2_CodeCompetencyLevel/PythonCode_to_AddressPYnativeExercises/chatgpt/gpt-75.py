# Given list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

# Create an empty dictionary to store the counts
count_dict = {}

# Iterate over each element in the list
for item in sample_list:
    # If the item is already in the dictionary, increment its count
    if item in count_dict:
        count_dict[item] += 1
    # Otherwise, add the item to the dictionary with a count of 1
    else:
        count_dict[item] = 1

# Output the dictionary with the count of each element
print("Printing count of each item", count_dict)
