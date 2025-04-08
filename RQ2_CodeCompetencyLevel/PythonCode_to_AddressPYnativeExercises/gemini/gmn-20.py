# Prompt the user to enter 5 float numbers separated by commas
user_input = input("Enter 5 float numbers separated by commas: ")

# Split the input string into a list of strings
numbers_str = user_input.split(",")

# Convert the list of strings to a list of floats
numbers = [float(num) for num in numbers_str]

# Print the list of float numbers
print(numbers)
