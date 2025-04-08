# Given list
list1 = [34, 54, 67, 89, 11, 43, 94]

# Remove the item at index 4
removed_item = list1.pop(4)
print("List After removing element at index 4:", list1)

# Add the removed item at the 2nd position (index 2)
list1.insert(2, removed_item)
print("List after Adding element at index 2:", list1)

# Add the removed item at the end of the list
list1.append(removed_item)
print("List after Adding element at last:", list1)
