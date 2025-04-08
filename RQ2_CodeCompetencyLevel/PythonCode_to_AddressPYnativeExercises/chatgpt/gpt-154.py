import numpy as np

# Create the sample array
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

# Print the original array
print("Printing Original array")
print(sampleArray)

# Case 1: Sort the array by the second row (index 1)
sorted_by_row = sampleArray[sampleArray[1, :].argsort()]

# Print the result of sorting by second row
print("\nSorting Original array by second row")
print(sorted_by_row)

# Case 2: Sort the array by the second column (index 1)
sorted_by_column = sampleArray[sampleArray[:, 1].argsort()]

# Print the result of sorting by second column
print("\nSorting Original array by second column")
print(sorted_by_column)
