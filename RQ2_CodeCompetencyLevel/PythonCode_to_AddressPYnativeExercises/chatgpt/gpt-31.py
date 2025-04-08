# Given number
number = 75869

# Initialize the count of digits
count = 0

# Use a while loop to count the digits
while number > 0:
    number //= 10  # Remove the last digit
    count += 1  # Increment the count

# Print the total number of digits
print(count)
