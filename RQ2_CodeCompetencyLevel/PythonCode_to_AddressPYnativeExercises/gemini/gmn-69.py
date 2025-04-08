def extract_integers(string):
    """Extracts integers from a string.

    Args:
        string: The input string.

    Returns:
        A string containing only the extracted integers.
    """

    integers = ''.join(char for char in string if char.isdigit())
    return integers

# Example usage
str1 = 'I am 25 years and 10 months old'
result = extract_integers(str1)
print(result)  # Output: 2510
