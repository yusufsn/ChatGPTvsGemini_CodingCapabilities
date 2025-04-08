def recursive_sum(n):
    """Calculates the sum of numbers from 0 to n recursively.

    Args:
        n: The upper limit of the sum.

    Returns:
        The sum of numbers from 0 to n.
    """

    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)

# Calculate the sum of numbers from 0 to 10
result = recursive_sum(10)

# Print the result
print(result)  # Output: 55
