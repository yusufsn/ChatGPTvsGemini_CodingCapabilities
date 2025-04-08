def calculate_result(number1, number2):
    """Calculates the product or sum of two numbers based on a condition.

    Args:
        number1 (int): The first number.
        number2 (int): The second number.

    Returns:
        int: The product of the numbers if it's less than or equal to 1000,
             otherwise their sum.
    """

    product = number1 * number2
    if product <= 1000:
        return product
    else:
        return number1 + number2

# Example usage:
number1 = 20
number2 = 30

result = calculate_result(number1, number2)
print("The result is", result)  # Output: The result is 600

number1 = 40
number2 = 30

result = calculate_result(number1, number2)
print("The result is", result)  # Output: The result is 70
