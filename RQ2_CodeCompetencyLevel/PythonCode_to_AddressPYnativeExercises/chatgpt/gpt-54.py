def middle_three_chars(input_str):
    # Find the starting index for the middle three characters
    start_index = len(input_str) // 2 - 1
    # Extract the middle three characters
    middle_chars = input_str[start_index:start_index + 3]
    return middle_chars

# Test case 1
str1 = "JhonDipPeta"
print("Output for str1:", middle_three_chars(str1))

# Test case 2
str2 = "JaSonAy"
print("Output for str2:", middle_three_chars(str2))
