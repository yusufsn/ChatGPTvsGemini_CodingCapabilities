# Recursive function to calculate the sum
def sum_recursive(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    else:
        # Recursive call: sum of n + sum of numbers up to n-1
        return n + sum_recursive(n - 1)

# Calling the function to calculate sum from 0 to 10
result = sum_recursive(10)
print(result)
