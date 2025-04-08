import re

def find_words_with_alphabets_and_numbers(s):
    # Use regular expression to find words that contain both alphabets and numbers
    return re.findall(r'\b\w*(?:[A-Za-z]+\d+|\d+[A-Za-z]+)\w*\b', s)

# Given string
str1 = "Emma25 is Data scientist50 and AI Expert"

# Call the function to find words with both alphabets and numbers
words_with_alphabets_and_numbers = find_words_with_alphabets_and_numbers(str1)

# Output the result
print("Words with both alphabets and numbers:")
for word in words_with_alphabets_and_numbers:
    print(word)
