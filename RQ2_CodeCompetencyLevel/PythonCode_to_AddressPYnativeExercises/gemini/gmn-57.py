def arrange_lowercase_first(str1):
  """Arranges lowercase letters first in a given string.

  Args:
    str1: The input string.

  Returns:
    The rearranged string with lowercase letters first.
  """

  lowercase_chars = []
  uppercase_chars = []

  for char in str1:
    if char.islower():
      lowercase_chars.append(char)
    else:
      uppercase_chars.append(char)

  return ''.join(lowercase_chars + uppercase_chars)

# Example usage
str1 = "PyNaTive"
print(arrange_lowercase_first(str1))  # Output: yaivePNT
