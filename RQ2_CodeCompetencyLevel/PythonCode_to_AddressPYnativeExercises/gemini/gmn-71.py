import re

def replace_special_symbols(string):
    """Replaces special symbols in a string with '#'

    Args:
        string: The input string.

    Returns:
        The string with special symbols replaced by '#'.
    """

    # Define a regular expression to match special symbols
    special_symbol_pattern = r"[^\w\s]"

    # Replace matched special symbols with '#'
    new_string = re.sub(special_symbol_pattern, "#", string)

    return new_string

# Example usage
str1 = '/*Jon is @developer & musician!!'
result = replace_special_symbols(str1)
print(result)  # Output: ##Jon is #developer # musician##
