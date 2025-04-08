def unique_values_from_dict(dictionary):
  """Gets unique values from a dictionary.

  Args:
    dictionary: The input dictionary.

  Returns:
    A list of unique values from the dictionary.
  """

  unique_values = list(set(dictionary.values()))
  return unique_values

# Example usage
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

unique_values = unique_values_from_dict(speed)
print(unique_values)
