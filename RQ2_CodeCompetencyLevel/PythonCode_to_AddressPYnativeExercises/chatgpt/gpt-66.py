def split_on_hyphens(s):
    # Split the string on hyphens and return the resulting list
    return s.split('-')

# Given string
str1 = "Emma-is-a-data-scientist"

# Call the function to split the string
substrings = split_on_hyphens(str1)

# Display each substring
print("Displaying each substring:")
for substring in substrings:
    print(substring)
