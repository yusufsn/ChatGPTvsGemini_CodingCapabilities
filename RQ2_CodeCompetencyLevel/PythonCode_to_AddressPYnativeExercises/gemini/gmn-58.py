def count_chars_digits_symbols(str1):
    """Counts the number of characters, digits, and symbols in a string.

    Args:
        str1: The input string.

    Returns:
        A tuple containing the counts of characters, digits, and symbols.
    """

    chars = digits = symbols = 0

    for char in str1:
        if char.isalpha():
            chars += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1

    return chars, digits, symbols

# Example usage
str1 = "P@#yn26at^&i5ve"
chars, digits, symbols = count_chars_digits_symbols(str1)

print("Chars =", chars)
print("Digits =", digits)
print("Symbols =", symbols)
