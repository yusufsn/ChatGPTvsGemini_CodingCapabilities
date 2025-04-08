import re

def count_occurrences(string, substring):
  """Counts the occurrences of a substring in a string, ignoring case.

  Args:
    string: The main string.
    substring: The substring to search for.

  Returns:
    The number of occurrences.
  """

  # Convert both strings to lowercase for case-insensitive matching
  string = string.lower()
  substring = substring.lower()

  # Use regular expressions to find all non-overlapping matches
  matches = re.findall(substring, string)

  return len(matches)

# Example usage
str1 = "Welcome to USA. usa awesome, isn't it?"
substring = "USA"

count = count_occurrences(str1, substring)
print("The USA count is:", count)  # Output: The USA count is: 2
