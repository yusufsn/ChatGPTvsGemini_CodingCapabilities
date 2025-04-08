# Loop to print the pattern
for i in range(1, 6):  # Outer loop controls the number of rows
    for j in range(1, i + 1):  # Inner loop prints numbers in each row
        print(j, end=" ")  # Print numbers in a row without newline
    print()  # Move to the next line after each row
