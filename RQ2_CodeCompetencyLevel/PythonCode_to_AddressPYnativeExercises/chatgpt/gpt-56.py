def create_new_string(s1, s2):
    # Get the first, middle, and last characters of s1
    first_s1 = s1[0]
    middle_s1 = s1[len(s1) // 2]
    last_s1 = s1[-1]
    
    # Get the first, middle, and last characters of s2
    first_s2 = s2[0]
    middle_s2 = s2[len(s2) // 2]
    last_s2 = s2[-1]
    
    # Combine the characters to form the new string
    new_string = first_s1 + first_s2 + middle_s1 + middle_s2 + last_s1 + last_s2
    return new_string

# Given strings
s1 = "America"
s2 = "Japan"

# Call the function
result = create_new_string(s1, s2)

print("The new string is:", result)
