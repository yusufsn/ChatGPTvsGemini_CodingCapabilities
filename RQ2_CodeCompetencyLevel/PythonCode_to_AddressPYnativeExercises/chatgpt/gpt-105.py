# Given sets# Given sets
set1 = {10, 20, 30}
set2 = {20, 40, 50}

# Update set1 with items that are only in set1 and not in set2
set1 -= set2

# Output the updated set1
print(set1)

set1 = {10, 20, 30}
set2 = {20, 40, 50}
  
# Update set1 with items that don't exist in set2
set1.difference_update(set2)
  
# Print the updated set1
print("set1", set1)
