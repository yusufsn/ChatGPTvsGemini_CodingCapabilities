def arrange_lowercase_first(input_str):
    # Separate the lowercase and uppercase letters
    lowercase_chars = [char for char in input_str if char.islower()]
    uppercase_chars = [char for char in input_str if char.isupper()]
    
    # Combine lowercase letters first, then uppercase letters
    arranged_str = ''.join(lowercase_chars) + ''.join(uppercase_chars)
    return arranged_str

# Given string
str1 = "PyNaTive"

# Call the function
result = arrange_lowercase_first(str1)

print("The arranged string is:", result)
