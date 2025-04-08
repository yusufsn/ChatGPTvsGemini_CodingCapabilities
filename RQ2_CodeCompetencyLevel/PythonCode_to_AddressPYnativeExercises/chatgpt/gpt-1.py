def calculate_result(number1, number2):
    product = number1 * number2
    if product <= 1000:
        return f"The result is {product}"
    else:
        return f"The result is {number1 + number2}"

# Example usage
number1 = 20
number2 = 30
print(calculate_result(number1, number2))  # Expected Output: The result is 600

number1 = 40
number2 = 30
print(calculate_result(number1, number2))  # Expected Output: The result is 70
