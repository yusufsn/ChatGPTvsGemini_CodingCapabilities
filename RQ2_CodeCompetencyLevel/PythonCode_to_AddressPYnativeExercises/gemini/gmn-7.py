def count_substring(string, substring):
  """Counts the number of occurrences of a substring in a string.

  Args:
    string: The main string.
    substring: The substring to count.

  Returns:
    The number of occurrences of the substring in the string.
  """

  count = string.count(substring)
  return count

# Example usage:
str_x = "Emma is good developer. Emma is a writer"
substring = "Emma"

count = count_substring(str_x, substring)
print(f"{substring} appeared 1  {count} times")
