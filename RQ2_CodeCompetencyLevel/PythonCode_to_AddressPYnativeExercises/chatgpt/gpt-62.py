def sum_and_average_of_digits(s1):
    # Extract digits from the string
    digits = [int(char) for char in s1 if char.isdigit()]
    
    # Calculate sum and average
    total_sum = sum(digits)
    average = total_sum / len(digits) if digits else 0  # Handle case if no digits found
    
    return total_sum, average

# Given string
str1 = "PYnative29@#8496"

# Call the function to calculate sum and average
total_sum, average = sum_and_average_of_digits(str1)

# Output the result
print(f"Sum is: {total_sum}")
print(f"Average is: {average}")
