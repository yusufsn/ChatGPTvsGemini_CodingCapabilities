set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Use the symmetric_difference() method to find elements in either set, but not both
unique_elements = set1.symmetric_difference(set2)

# Update set1 with the unique elements
set1.update(unique_elements)

print(set1)
