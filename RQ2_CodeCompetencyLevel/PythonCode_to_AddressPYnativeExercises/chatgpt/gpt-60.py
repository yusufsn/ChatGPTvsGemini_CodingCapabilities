def are_strings_balanced(s1, s2):
    # Convert both strings to sets to check if s1's characters are in s2
    return all(char in s2 for char in s1)

# Test case 1
s1 = "Yn"
s2 = "PYnative"
print("Test Case 1: ", are_strings_balanced(s1, s2))  # Expected Output: True

# Test case 2
s1 = "Ynf"
s2 = "PYnative"
print("Test Case 2: ", are_strings_balanced(s1, s2))  # Expected Output: False
