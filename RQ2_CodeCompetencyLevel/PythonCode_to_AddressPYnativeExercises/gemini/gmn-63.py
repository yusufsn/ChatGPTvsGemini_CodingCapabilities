def count_char_occurrences(string):
    """Counts the occurrences of each character in a string.

    Args:
        string: The input string.

    Returns:
        A dictionary containing character frequencies.
    """

    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

# Example usage
str1 = "Apple"
char_counts = count_char_occurrences(str1)
print(char_counts)  # Output: {'A': 1, 'p': 2, 'l': 1, 'e': 1}
