def reverse_digits(number):
    # Convert the number to a string, reverse it, and join the digits with spaces
    return ' '.join(str(number)[::-1])

# Example usage
number = 7536
result = reverse_digits(number)

# Display the result
print(result)
