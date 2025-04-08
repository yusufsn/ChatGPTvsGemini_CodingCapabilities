import re

def find_mixed_words(string):
    """Finds words containing both alphabets and numbers.

    Args:
        string: The input string.

    Returns:
        A list of words containing both alphabets and numbers.
    """

    pattern = r'\w*[a-zA-Z]+\w*[0-9]+\w*'
    mixed_words = re.findall(pattern, string)
    return mixed_words

# Example usage
str1 = "Emma25 is Data scientist50 and AI Expert"
mixed_words = find_mixed_words(str1)
print(mixed_words)  # Output: ['Emma25', 'scientist50']
