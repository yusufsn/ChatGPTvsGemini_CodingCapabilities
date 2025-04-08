def filter_list_by_dict(roll_number, sample_dict):
  """Filters a list based on dictionary values.

  Args:
    roll_number: The input list of roll numbers.
    sample_dict: The dictionary containing names and roll numbers.

  Returns:
    The filtered list.
  """

  filtered_list = []
  for roll_num in roll_number:
    if roll_num in sample_dict.values():
      filtered_list.append(roll_num)
  return filtered_list

# Example usage
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

filtered_list = filter_list_by_dict(roll_number, sample_dict)
print("After removing unwanted elements from list", filtered_list)
