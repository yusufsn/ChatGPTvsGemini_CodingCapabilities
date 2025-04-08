def exponent(base, exp):
  """Calculates the exponent of a number.

  Args:
    base: The base number.
    exp: The exponent.

  Returns:
    The result of base raised to the power of exp.
  """

  result = 1
  for _ in range(exp):
    result *= base
  return result

# Example usage:
base = 2
exponent = 5
print(f"{base} raises to the power of {exponent}: {exponent(base, exponent)}")

base = 5
exponent = 4
print(f"{base} raises to the power of {exponent} is: {exponent(base, exponent)}")
