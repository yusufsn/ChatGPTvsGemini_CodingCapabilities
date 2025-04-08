def reverse_digits(number):
  """Reverses the digits of a number and prints them.

  Args:
    number: The input number.
  """

  while number > 0:
    digit = number % 10
    print(digit, end=" ")
    number //= 10

# Example usage:
num = 7536
reverse_digits(num)
