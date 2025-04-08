def skip_line_and_write(input_file, output_file, line_to_skip):
  """
  Reads the content of an input file, skips the specified line, and writes the remaining content to an output file.

  Args:
    input_file: The name of the input file.
    output_file: The name of the output file.
    line_to_skip: The line number to skip (1-indexed).
  """

  with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    for line_num, line in enumerate(f_in, 1):
      if line_num != line_to_skip:
        f_out.write(line)

# Example usage:
input_file = 'test.txt'
output_file = 'new_file.txt'
line_to_skip = 5

skip_line_and_write(input_file, output_file, line_to_skip)
