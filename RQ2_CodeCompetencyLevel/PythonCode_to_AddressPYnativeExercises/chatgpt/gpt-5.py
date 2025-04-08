def check_first_last(numbers):
    # Check if the list has at least one element
    if len(numbers) < 1:
        return "Error: List is empty"
    # Compare the first and last elements
    return numbers[0] == numbers[-1]

# Given lists
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

# Display results
print("Given list:", numbers_x)
print("Result is", check_first_last(numbers_x))  # Expected Output: True

print("Given list:", numbers_y)
print("Result is", check_first_last(numbers_y))  # Expected Output: False
