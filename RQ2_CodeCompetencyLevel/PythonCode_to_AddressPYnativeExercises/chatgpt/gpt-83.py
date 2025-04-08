# Given lists
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# Concatenate lists index-wise
concatenated_list = [a + b for a, b in zip(list1, list2)]

# Add any leftover items from the longer list
concatenated_list.extend(list1[len(list2):] or list2[len(list1):])

# Display the result
print(concatenated_list)
