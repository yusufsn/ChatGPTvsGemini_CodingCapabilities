import re

def count_occurrences(substring, string):
    # Use re.IGNORECASE to ignore case while searching for the substring
    return len(re.findall(substring, string, re.IGNORECASE))

# Given string
str1 = "Welcome to USA. usa awesome, isn't it?"

# Substring to search for
substring = "USA"

# Call the function to count occurrences
count = count_occurrences(substring, str1)

# Output the result
print(f"The USA count is: {count}")
