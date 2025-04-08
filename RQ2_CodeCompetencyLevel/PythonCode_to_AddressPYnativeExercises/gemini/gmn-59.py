def mix_strings(s1, s2):
    """Mixes two strings based on the given rule.

    Args:
        s1: The first string.
        s2: The second string.

    Returns:
        The mixed string.
    """

    result = ""
    i, j = 0, len(s2) - 1

    while i < len(s1) and j >= 0:
        result += s1[i] + s2[j]
        i += 1
        j -= 1

    # Add any leftover characters
    result += s1[i:] + s2[:j + 1]

    return result

# Example usage
s1 = "Abc"
s2 = "Xyz"
print(mix_strings(s1, s2))  # Output: AzbycX
