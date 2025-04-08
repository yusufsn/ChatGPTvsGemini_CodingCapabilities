# Number of terms to display in the Fibonacci series
terms = 10

# Initial two numbers of the Fibonacci series
a, b = 0, 1

# Print the Fibonacci series up to 10 terms
print("Fibonacci sequence:")
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b  # Update the values of a and b for the next term
