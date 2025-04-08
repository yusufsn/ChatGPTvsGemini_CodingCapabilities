# Loop to print the reverse pattern
for i in range(5, 0, -1):  # Start from 5 and go down to 1
    for j in range(i, 0, -1):  # Inner loop to print numbers from i to 1
        print(j, end=" ")  # Print numbers in a row without a newline
    print()  # Move to the next line after each row
