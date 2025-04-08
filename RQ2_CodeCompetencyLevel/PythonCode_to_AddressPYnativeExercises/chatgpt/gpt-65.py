def find_last_position(substring, string):
    # Use rfind() to find the last occurrence of the substring
    return string.rfind(substring)

# Given string
str1 = "Emma is a data scientist who knows Python. Emma works at google."

# Substring to search for
substring = "Emma"

# Call the function to find the last position
last_position = find_last_position(substring, str1)

# Output the result
print(f"Last occurrence of {substring} starts at index {last_position}")
