def show_employee(name, salary=9000):
    """Displays employee information.

    Args:
        name: The employee's name.
        salary: The employee's salary, defaults to 9000.
    """

    print("Name:", name, "salary:", salary)

# Call the function with both arguments
show_employee("Ben", 12000)

# Call the function with only the name argument
show_employee("Jessa")
