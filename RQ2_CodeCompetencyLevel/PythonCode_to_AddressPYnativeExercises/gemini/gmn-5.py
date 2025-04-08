def check_first_last(numbers):
  """Checks if the first and last numbers in a list are the same.

  Args:
    numbers: The list of numbers.

  Returns:
    True if the first and last numbers are the same, False otherwise.
  """

  return numbers[0] == numbers[-1]

# Example usage:
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print("Given list:", numbers_x)
print("result is", check_first_last(numbers_x))

print("\nGiven list:", numbers_y)
print("result is", check_first_last(numbers_y))
