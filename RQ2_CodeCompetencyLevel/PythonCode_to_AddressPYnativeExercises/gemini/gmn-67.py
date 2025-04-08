def remove_empty_strings(str_list):
    """Removes empty strings from a list of strings.

    Args:
        str_list: The list of strings.

    Returns:
        A new list without empty strings.
    """

    return [string for string in str_list if string]

# Example usage
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print("Original list of strings:")
print(str_list)

filtered_list = remove_empty_strings(str_list)
print("After removing empty strings:")
print(filtered_list)
