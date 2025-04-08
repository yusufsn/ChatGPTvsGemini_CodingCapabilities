def is_balanced(s1, s2):
  """Checks if two strings are balanced.

  Args:
    s1: The first string.
    s2: The second string.

  Returns:
    True if the strings are balanced, False otherwise.
  """

  # Create a set of characters from s2 for efficient lookup
  s2_set = set(s2)

  # Check if each character in s1 is present in s2_set
  for char in s1:
    if char not in s2_set:
      return False

  return True

# Example usage
s1 = "Yn"
s2 = "PYnative"
print(is_balanced(s1, s2))  # Output: True

s1 = "Ynf"
s2 = "PYnative"
print(is_balanced(s1, s2))  # Output: False
