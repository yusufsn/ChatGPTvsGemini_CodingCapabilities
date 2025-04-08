import re

def remove_special_symbols(s):
    # Use regex to remove all characters that are not letters, digits, or spaces
    return re.sub(r'[^a-zA-Z0-9\s]', '', s)

# Given string
str1 = "/*Jon is @developer & musician"

# Call the function to remove special symbols
cleaned_str = remove_special_symbols(str1)

# Output the result
print(cleaned_str)
