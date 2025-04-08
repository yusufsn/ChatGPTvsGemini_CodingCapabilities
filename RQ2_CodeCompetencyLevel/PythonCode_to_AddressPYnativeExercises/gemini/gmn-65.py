def find_last_occurrence(string, substring):
    """Finds the last occurrence of a substring in a string.

    Args:
        string: The main string.
        substring: The substring to search for.

    Returns:
        The last index of the substring, or -1 if not found.
    """

    last_index = string.rfind(substring)
    return last_index

# Example usage
str1 = "Emma is a data scientist who knows Python. Emma works at google."
substring = "Emma"

last_index = find_last_occurrence(str1, substring)

if last_index != -1:
    print(f"Last occurrence of {substring} starts at index {last_index}")
else:
    print(f"{substring} not found in the string.")
