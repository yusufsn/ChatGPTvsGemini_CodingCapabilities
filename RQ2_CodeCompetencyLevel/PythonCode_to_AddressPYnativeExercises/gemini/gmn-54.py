def middle_three(str1):
    """Extracts the middle three characters from a given string.

    Args:
        str1: The input string.

    Returns:
        The string containing the middle three characters.
    """

    middle_index = len(str1) // 2
    start_index = middle_index - 1
    end_index = middle_index + 2
    return str1[start_index:end_index]

# Example usage
str1 = "JhonDipPeta"
str2 = "JaSonAy"

print(middle_three(str1))  # Output: Dip
print(middle_three(str2))  # Output: Son
