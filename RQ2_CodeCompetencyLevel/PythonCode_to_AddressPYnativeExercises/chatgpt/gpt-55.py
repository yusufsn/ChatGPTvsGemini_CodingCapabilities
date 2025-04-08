def append_in_middle(s1, s2):
    # Find the middle index of s1
    middle_index = len(s1) // 2
    # Create a new string by inserting s2 in the middle of s1
    s3 = s1[:middle_index] + s2 + s1[middle_index:]
    return s3

# Given strings
s1 = "Ault"
s2 = "Kelly"

# Call the function
s3 = append_in_middle(s1, s2)

print("The new string is:", s3)
