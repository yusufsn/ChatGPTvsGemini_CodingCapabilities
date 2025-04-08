set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Use the intersection() method to find common elements
common_elements = set1.intersection(set2)

if common_elements:
    print("Two sets have items in common")
    print(common_elements)
else:
    print("Two sets have no items in common")
