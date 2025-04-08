def combine_first_middle_last(s1, s2):
  """Combines the first, middle, and last characters of two strings.

  Args:
    s1: The first string.
    s2: The second string.

  Returns:
    The new string combining the specified characters.
  """

  middle1 = len(s1) // 2
  middle2 = len(s2) // 2

  new_string = s1[0] + s2[0] + s1[middle1] + s2[middle2] + s1[-1] + s2[-1]
  return new_string

# Example usage
s1 = "America"
s2 = "Japan"
print(combine_first_middle_last(s1, s2))  # Output: AJrpan
