def is_palindrome(number):
  """Checks if a number is a palindrome.

  Args:
    number: The number to check.

  Returns:
    True if the number is a palindrome, False otherwise.
  """

  original_num = number
  reverse_num = 0

  while number > 0:
    remainder = number % 10
    reverse_num = reverse_num * 10 + remainder
    number //= 10

  return original_num == reverse_num

# Example usage:
num1 = 121
num2 = 125

print("original number", num1)
print("Yes. given number is palindrome number" if is_palindrome(num1) else "No. given number is not palindrome number")

print("\noriginal number", num2)
print("Yes. given number is palindrome number" if is_palindrome(num2) else "No. given number is not palindrome number")
