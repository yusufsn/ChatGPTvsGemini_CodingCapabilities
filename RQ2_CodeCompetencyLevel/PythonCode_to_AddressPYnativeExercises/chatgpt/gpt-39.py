# Given number
num = 76542

# Reverse the number
reversed_num = 0

while num > 0:
    digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Build the reversed number
    num //= 10  # Remove the last digit

# Print the reversed number
print(reversed_num)
