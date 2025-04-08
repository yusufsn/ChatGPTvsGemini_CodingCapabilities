set1 = {10, 20, 30}
set2 = {20, 40, 50}

# Use the difference_update() method to remove elements from set1 that are present in set2
set1.difference_update(set2)

print(set1)
