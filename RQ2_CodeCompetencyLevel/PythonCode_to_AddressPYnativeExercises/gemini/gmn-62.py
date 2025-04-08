def sum_and_average_of_digits(string):
    """Calculates the sum and average of digits in a string.

    Args:
        string: The input string.

    Returns:
        A tuple containing the sum and average of digits.
    """

    digit_sum = 0
    digit_count = 0

    for char in string:
        if char.isdigit():
            digit_sum += int(char)
            digit_count += 1

    if digit_count == 0:
        return 0, 0

    average = digit_sum / digit_count
    return digit_sum, average

# Example usage
str1 = "PYnative29@#8496"
sum, average = sum_and_average_of_digits(str1)

print("Sum is:", sum)
print("Average is:", average)
