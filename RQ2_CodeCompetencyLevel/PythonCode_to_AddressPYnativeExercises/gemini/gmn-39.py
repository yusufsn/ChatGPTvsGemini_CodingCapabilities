def reverse_integer(num):
  """Reverses the digits of an integer.

  Args:
    num: The integer to reverse.

  Returns:
    The reversed integer.
  """

  reversed_num = 0
  while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
  return reversed_num

# Get the number from the user
num = int(input("Enter a number: "))

# Reverse the number
reversed_num = reverse_integer(num)

# Print the reversed number
print("Reversed number:", reversed_num)
