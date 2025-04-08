def remove_chars(input_string, n):
    # Ensure n is less than the length of the string
    if n >= len(input_string):
        return "Error: n must be less than the length of the string"
    return input_string[n:]

# Example usage
print(remove_chars("PYnative", 4))  # Output: tive
print(remove_chars("PYnative", 2))  # Output: native
