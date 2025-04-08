# Given sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Remove common items and update set1
set1.symmetric_difference_update(set2)

# Output the result
print(set1)
