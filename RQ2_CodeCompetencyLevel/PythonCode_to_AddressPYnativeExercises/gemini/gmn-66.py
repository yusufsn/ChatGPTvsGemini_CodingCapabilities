def split_on_hyphens(string):
    """Splits a string on hyphens and prints each substring.

    Args:
        string: The input string.
    """

    substrings = string.split('-')
    for substring in substrings:
        print(substring)

# Example usage
str1 = "Emma-is-a-data-scientist"
split_on_hyphens(str1)
