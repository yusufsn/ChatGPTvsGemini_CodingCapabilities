def pair_elements(first_list, second_list):
  """Pairs elements from two lists into a set.

  Args:
    first_list: The first list.
    second_list: The second list.

  Returns:
    A set of tuples, where each tuple contains a pair of elements from the input lists.
  """

  return set(zip(first_list, second_list))

# Example usage
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result = pair_elements(first_list, second_list)
print("Result is", result)
