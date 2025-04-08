# Get input from the user, separated by spaces
user_input = input("Enter three names separated by spaces: ")

# Split the input string into a list of names
names = user_input.split()

# Check if the user entered exactly three names
if len(names) != 3:
    print("Please enter exactly three names.")
else:
    # Print the names
    print("Name1:", names[0])
    print("Name2:", names[1])
    print("Name3:", names[2])
