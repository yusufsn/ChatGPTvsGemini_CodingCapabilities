import re

# Given string
str1 = '/*Jon is @developer & musician!!'

# Replace all special characters (anything that's not a letter, number, or space) with '#'
result = re.sub(r'[^a-zA-Z0-9\s]', '#', str1)

# Print the result
print(result)
