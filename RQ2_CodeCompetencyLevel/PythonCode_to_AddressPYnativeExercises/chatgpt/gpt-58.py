def count_chars_digits_symbols(input_str):
    # Initialize counts for characters, digits, and symbols
    chars_count = 0
    digits_count = 0
    symbols_count = 0

    # Loop through each character in the input string
    for char in input_str:
        if char.isalpha():  # Check if the character is a letter
            chars_count += 1
        elif char.isdigit():  # Check if the character is a digit
            digits_count += 1
        else:  # The character is a symbol
            symbols_count += 1

    return chars_count, digits_count, symbols_count

# Given string
str1 = "P@#yn26at^&i5ve"

# Call the function
chars, digits, symbols = count_chars_digits_symbols(str1)

# Print the result
print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbols = {symbols}")
