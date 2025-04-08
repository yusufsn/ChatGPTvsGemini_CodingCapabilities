def fibonacci_series(n):
  """Generates the Fibonacci series up to the nth term.

  Args:
    n: The number of terms to generate.

  Returns:
    A list containing the Fibonacci series up to the nth term.
  """

  fib_series = [0, 1]
  for i in range(2, n):
    next_fib = fib_series[i - 1] + fib_series[i - 2]
    fib_series.append(next_fib)
  return fib_series

n  = 10
fib_series = fibonacci_series(n)
print("Fibonacci sequence:")
print(*fib_series)
