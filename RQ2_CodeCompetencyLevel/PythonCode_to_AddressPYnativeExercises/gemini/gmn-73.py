def manipulate_list(list1):
  """Removes an item at index 4, adds it to index 2 and the end.

  Args:
    list1: The input list.

  Returns:
    The modified list.
  """

  # Remove the item at index 4
  removed_item = list1.pop(4)

  # Add the removed item at index 2
  list1.insert(2, removed_item)

  # Add the removed item at the end
  list1.append(removed_item)

  return list1

# Example usage
list1 = [34, 54, 67, 89, 11, 43, 94]

print("List After removing element at index 4", list1.copy())
list1 = manipulate_list(list1)
print("List after Adding element at index 2", list1.copy())
list1 = manipulate_list(list1)
print("List after Adding element at last", list1)
