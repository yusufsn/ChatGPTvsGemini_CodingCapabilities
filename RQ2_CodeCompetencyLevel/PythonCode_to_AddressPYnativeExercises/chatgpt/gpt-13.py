def print_multiplication_table():
    # Loop through numbers 1 to 10 for rows
    for i in range(1, 11):
        # For each row, print the multiplication results from 1 to 10
        for j in range(1, 11):
            print(i * j, end=" ")  # Print the product, followed by a space
        print()  # Print a new line after each row

# Call the function to print the table
print_multiplication_table()
