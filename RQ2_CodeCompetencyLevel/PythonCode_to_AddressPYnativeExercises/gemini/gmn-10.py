def merge_lists(list1, list2):
  """Merges two lists, taking odd numbers from the first and even numbers from the second.

  Args:
    list1: The first list of numbers.
    list2: The second list of numbers.

  Returns:
    A new list containing the merged numbers.
  """

  merged_list = []
  for num in list1:
    if num % 2 != 0:
      merged_list.append(num)
  for num in list2:
    if num % 2 == 0:
      merged_list.append(num)
  return merged_list

# Example usage:
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

result_list = merge_lists(list1, list2)
print("result list:", result_list)
