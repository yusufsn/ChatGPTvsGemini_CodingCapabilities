def remove_all_occurrences(list1, item_to_remove):
  """Removes all occurrences of a specific item from a list.

  Args:
    list1: The input list.
    item_to_remove: The item to remove.

  Returns:
    A new list with the specified item removed.
  """

  return [x for x in list1 if x != item_to_remove]

# Example usage:
list1 = [5, 20, 15, 20, 25, 50, 20]
item_to_remove = 20

new_list = remove_all_occurrences(list1, item_to_remove)
print(new_list)  # Output: [5, 15, 25, 50]
