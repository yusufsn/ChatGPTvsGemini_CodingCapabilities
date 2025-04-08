def remove_non_integers(s):
    # Use a list comprehension to keep only the digits
    return ''.join([char for char in s if char.isdigit()])

# Given string
str1 = 'I am 25 years and 10 months old'

# Call the function to remove non-integer characters
result = remove_non_integers(str1)

# Output the result
print(result)
