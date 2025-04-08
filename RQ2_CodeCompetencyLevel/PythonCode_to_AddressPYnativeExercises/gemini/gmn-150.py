import numpy as np

# Sample array
sampleArray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

# Print the input array
print("Printing Input Array")
print(sampleArray)

# Extract the third column 1 
third_column = sampleArray[:, 2]

# Print the extracted column
print("\nPrinting array of items in the third column from all rows")
print(third_column)
