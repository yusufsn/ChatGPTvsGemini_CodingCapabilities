from collections import Counter

def count_characters(s):
    # Use Counter to count occurrences of all characters
    return dict(Counter(s))

# Given string
str1 = "Apple"

# Call the function to count occurrences
character_counts = count_characters(str1)

# Output the result
print(character_counts)
