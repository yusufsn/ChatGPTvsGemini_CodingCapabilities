def print_star_pattern(rows):
    """Prints a star pattern with increasing and then decreasing number of stars.

    Args:
        rows: The number of rows in the pattern.
    """

    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()

    for i in range(rows - 1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

# Get the desired number of rows from the user
rows = int(input("Enter the number of rows: "))

# Print the star pattern
print_star_pattern(rows)
