import numpy as np

# Provided NumPy array
sampleArray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

# Print the input array
print("Printing Input Array")
print(sampleArray)

# Extract and print the third column (index 2)
third_column = sampleArray[:, 2]
print("\nPrinting array of items in the third column from all rows")
print(third_column)
