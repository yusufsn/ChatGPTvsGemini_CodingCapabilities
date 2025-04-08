def print_half_pyramid():
    # Number of rows in the pyramid
    rows = 5
    
    # Loop through the rows in reverse order
    for i in range(rows, 0, -1):
        # Print stars in each row
        print('* ' * i)

# Call the function to print the pattern
print_half_pyramid()
