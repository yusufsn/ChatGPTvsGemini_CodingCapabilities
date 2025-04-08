def count_occurrences(sample_list):
  """Counts the occurrences of each element in a list.

  Args:
    sample_list: The input list.

  Returns:
    A dictionary containing element-count pairs.
  """

  element_counts = {}
  for element in sample_list:
    element_counts[element] = element_counts.get(element, 0) + 1
  return element_counts

# Example usage
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

result = count_occurrences(sample_list)
print("Printing count of each item", result)
