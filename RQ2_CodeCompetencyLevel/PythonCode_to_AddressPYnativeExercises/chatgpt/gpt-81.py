# Given list
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

# Remove duplicates by converting the list to a set and then back to a list
unique_items = list(set(sample_list))

# Sort the list to ensure it maintains a consistent order
unique_items.sort()

# Create a tuple from the unique items
unique_tuple = tuple(unique_items)

# Find the minimum and maximum
min_value = min(unique_items)
max_value = max(unique_items)

# Display the results
print("unique items:", unique_items)
print("tuple:", unique_tuple)
print("min:", min_value)
print("max:", max_value)
