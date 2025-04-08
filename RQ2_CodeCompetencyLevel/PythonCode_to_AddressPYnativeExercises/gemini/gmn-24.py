import os

def is_file_empty(file_path):
  """Checks if a given file is empty.

  Args:
    file_path: The path to the file.

  Returns:
    True if the file is empty, False otherwise.
  """

  return os.stat(file_path).st_size == 0

# Example usage:
file_path = 'new_file.txt'  # Replace with the actual file path

if is_file_empty(file_path):
  print("The file is empty.")
else:
  print("The file is not empty.")
