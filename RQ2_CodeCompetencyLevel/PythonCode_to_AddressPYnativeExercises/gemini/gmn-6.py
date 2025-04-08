def display_divisible_by_5(numbers):
  """Displays numbers from a list that are divisible by 5.

  Args:
    numbers: The list of numbers.
  """

  print("Given list is", numbers)
  print("Divisible by 5")
  for num in numbers:
    if num % 5 == 0:
      print(num)

# Example usage:
numbers = [10, 20, 33, 46, 55]
display_divisible_by_5(numbers)
