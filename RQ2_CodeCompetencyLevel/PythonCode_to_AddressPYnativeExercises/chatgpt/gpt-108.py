# Given sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Find the intersection (common elements) between the two sets
common_elements = set1.intersection(set2)

# Check if there are any common elements
if common_elements:
    print("Two sets have items in common")
    print(common_elements)
else:
    print("No common elements")
