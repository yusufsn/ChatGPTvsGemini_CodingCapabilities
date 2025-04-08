def factorial(n):
  """Calculates the factorial of a given number.

  Args:
    n: The number to calculate the factorial of.

  Returns:
    The factorial of the number.
  """

  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers.")
  elif n == 0:
    return 1
  else:
    factorial = 1
    for i in range(1, n + 1):
      factorial *= i
    return factorial

# Get the number from the user
num = int(input("Enter a number: "))

# Calculate the factorial
result = factorial(num)

# Print the result
print("The factorial of", num, "is", result)
