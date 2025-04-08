def sum_of_series(n):
  """Calculates the sum of the series up to n terms.

  Args:
    n: The number of terms.

  Returns:
    The sum of the series.
  """

  sum = 0
  term = 2
  for i in range(1, n + 1):
    sum += term
    term = term * 10 + 2
  return sum

n = 5
result = sum_of_series(n)
print("Sum of the series up to", n, "terms:", result)
