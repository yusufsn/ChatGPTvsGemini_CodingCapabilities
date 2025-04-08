sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

# Remove duplicates using a set
unique_items = list(set(sample_list))

# Create a tuple from the unique items
unique_tuple = tuple(unique_items)

# Find the minimum and maximum 1  values
min_value = min(unique_tuple)
max_value = max(unique_tuple)

print("Unique items:", unique_items)
print("Tuple:", unique_tuple)
print("min:", min_value)
print("max:", max_value)
