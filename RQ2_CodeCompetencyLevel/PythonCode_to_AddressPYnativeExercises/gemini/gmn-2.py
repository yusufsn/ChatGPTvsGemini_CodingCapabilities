def print_sum_of_current_and_previous(n):
  """Prints the sum of the current and previous number for the first n numbers.

  Args:
    n: The number of iterations.
  """

  previous_number = 0
  for current_number in range(n):
    sum = current_number + previous_number
    print(f"Current Number {current_number} Previous Number {previous_number} Sum: {sum}")
    previous_number = current_number

# Example usage:
print_sum_of_current_and_previous(10)
