def read_line_number(file_path, line_number):
  """Reads the specified line number from a file.

  Args:
    file_path: The path to the file.
    line_number: The line number to read (1-indexed).

  Returns:
    The content of the specified line, or None if the line number is invalid.
  """

  with open(file_path, 'r') as f:
    for i, line in enumerate(f, 1):
      if i == line_number:
        return line.strip()
  return None

# Example usage:
file_path = 'test.txt'
line_number = 4

line_content = read_line_number(file_path, line_number)

if line_content:
  print(f"Line {line_number}: {line_content}")
else:
  print(f"Line {line_number} not found in the file.")
