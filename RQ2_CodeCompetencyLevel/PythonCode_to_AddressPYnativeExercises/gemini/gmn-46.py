def calculation(a, b):
    """Calculates the sum and difference of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        A tuple containing the sum and difference.
    """

    addition = a + b
    subtraction = a - b
    return addition, subtraction

# Get the result from the function
res = calculation(40, 10)

# Print the result
print(res)
