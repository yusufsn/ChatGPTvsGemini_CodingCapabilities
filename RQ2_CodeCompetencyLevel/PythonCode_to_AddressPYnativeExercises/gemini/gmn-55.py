def append_middle(s1, s2):
  """Appends s2 in the middle of s1.

  Args:
    s1: The first string.
    s2: The second string.

  Returns:
    The new string with s2 appended in the middle of s1.
  """

  middle_index = len(s1) // 2
  return s1[:middle_index] + s2 + s1[middle_index:]

# Example usage
s1 = "Ault"
s2 = "Kelly"
print(append_middle(s1, s2))  # Output: AuKellylt
