import numpy as np

# Create the sample array and the new column to insert
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
newColumn = np.array([10, 10, 10]).reshape(-1, 1)  # Reshaping to make it a column

# Print the original array
print("Printing Original array")
print(sampleArray)

# Delete the second column (index 1)
array_after_deletion = np.delete(sampleArray, 1, axis=1)

# Print the array after deleting the second column
print("\nArray after deleting column 2 on axis 1")
print(array_after_deletion)

# Insert the new column at index 1
array_after_insertion = np.insert(array_after_deletion, 1, newColumn, axis=1)

# Print the array after inserting the new column
print("\nArray after inserting column 2 on axis 1")
print(array_after_insertion)
