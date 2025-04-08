set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Find the intersection of the two sets
common_elements = set1.intersection(set2)

# Update set1 to only contain common elements
set1.intersection_update(common_elements)

print(set1)  # Output: {30, 40, 50}
