def create_mixed_string(s1, s2):
    # Initialize an empty list to store the characters of the new string
    mixed_str = []
    
    # Find the minimum length of both strings to avoid index out of range
    min_len = min(len(s1), len(s2))
    
    # Loop through the characters of both strings
    for i in range(min_len):
        mixed_str.append(s1[i])  # Add char from s1
        mixed_str.append(s2[-(i+1)])  # Add char from s2 (starting from the end)
    
    # Append any leftover characters from the longer string
    mixed_str.append(s1[min_len:])  # Add remaining chars from s1
    mixed_str.append(s2[:len(s2)-min_len])  # Add remaining chars from s2
    
    # Join the list to form the final string
    return ''.join(mixed_str)

# Given strings
s1 = "Abc"
s2 = "Xyz"

# Call the function
result = create_mixed_string(s1, s2)

print("The mixed string is:", result)
