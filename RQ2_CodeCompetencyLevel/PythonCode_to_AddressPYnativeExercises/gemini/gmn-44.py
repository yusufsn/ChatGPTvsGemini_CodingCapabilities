def print_name_age(name, age):
    """Prints the given name and age.

    Args:
        name: The person's name.
        age: The person's age.
    """

    print("Name:", name)
    print("Age:", age)

# Get the name and age from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Call the function to print the information
print_name_age(name, age)
