import numpy as np

# Create the sample array
sampleArray = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])

# Create the new column
newColumn = np.array([[10], [10], [10]])

# Print the original array
print("Printing Original array")
print(sampleArray)

# Delete the second column (index 1)
array_without_column = np.delete(sampleArray, 1, axis=1)
print("\nArray after deleting column 2 on axis 1")
print(array_without_column)

# Insert the new column at index 1
array_with_new_column = np.insert(array_without_column, 1, newColumn, axis=1)
print("\nArray after inserting column 2 on axis 1")
print(array_with_new_column)
