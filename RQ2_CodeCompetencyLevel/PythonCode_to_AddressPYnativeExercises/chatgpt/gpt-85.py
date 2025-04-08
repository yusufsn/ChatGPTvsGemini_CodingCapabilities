# Given lists
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# Concatenate lists in the desired order
concatenated_list = [a + b for a in list1 for b in list2]

# Display the result
print(concatenated_list)
