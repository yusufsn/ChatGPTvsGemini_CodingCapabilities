def outer_function(a, b):
    """Outer function to calculate the addition.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a, b, and 5.
    """

    def inner_function(a, b):
        """Inner function to calculate the addition of a and b.

        Args:
            a: The first number.
            b: The second number.

        Returns:
            The sum of a and b.
        """

        return a + b

    addition = inner_function(a, b)
    return addition + 5

# Get the result from the outer function
result = outer_function(10, 20)

# Print the result
print(result)  # Output: 35
