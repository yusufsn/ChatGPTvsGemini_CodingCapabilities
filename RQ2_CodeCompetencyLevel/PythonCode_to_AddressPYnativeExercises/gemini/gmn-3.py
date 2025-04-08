def print_even_index_chars(string):
  """Prints characters at even indices in a given string.

  Args:
    string: The input string.
  """

  print("Original String is", string)
  print("Printing only even index chars")
  for i in range(0, len(string), 2):
    print(string[i])

# Example usage:
user_input = input("Enter a string: ")
print_even_index_chars(user_input)
