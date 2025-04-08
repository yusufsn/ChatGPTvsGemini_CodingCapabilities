import re

def remove_special_symbols(string):
    """Removes special symbols and punctuation from a string.

    Args:
        string: The input string.

    Returns:
        The string without special symbols and punctuation.
    """

    return re.sub(r'[^\w\s]', '', string)

# Example usage
str1 = "/*Jon is @developer & musician"
result = remove_special_symbols(str1)
print(result)  # Output: "Jon is developer musician"
