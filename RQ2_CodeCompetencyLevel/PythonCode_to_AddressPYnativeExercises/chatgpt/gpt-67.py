def remove_empty_strings(str_list):
    # Remove empty strings and None values from the list
    return [item for item in str_list if item != "" and item is not None]

# Given list
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# Output the original list
print("Original list of strings:")
print(str_list)

# Call the function to remove empty strings
filtered_list = remove_empty_strings(str_list)

# Output the list after removing empty strings
print("\nAfter removing empty strings:")
print(filtered_list)
