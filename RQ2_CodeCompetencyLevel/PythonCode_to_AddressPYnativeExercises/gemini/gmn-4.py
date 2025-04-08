def remove_chars(string, n):
  """Removes the first n characters from a string.

  Args:
    string: The input string.
    n: The number of characters to remove.

  Returns:
    The string with the first n characters removed.

  Raises:
    ValueError: If n is greater than or equal to the length of the string.
  """

  if n >= len(string):
    raise ValueError("n must be less than the length of the string")
  return string[n:]

# Example usage:
string1 = "PYnative"
n1 = 4
new_string1 = remove_chars(string1, n1)
print(new_string1)  # Output: tive

string2 = "PYnative"
n2 = 2
new_string2 = remove_chars(string2, n2)
print(new_string2)  # Output: native
