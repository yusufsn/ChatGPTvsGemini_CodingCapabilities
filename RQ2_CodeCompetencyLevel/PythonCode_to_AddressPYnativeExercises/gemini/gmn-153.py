import numpy as np

# Create the 8x3 array
array = np.arange(10, 34).reshape(8, 3)

# Print the array
print("Creating 8X3 array using numpy.arange")
print(array)

# Split the array into 4 equal-sized sub-arrays
sub_arrays = np.split(array, 4)

# Print the sub-arrays
print("\nDividing 8X3 array into 4 sub array")
print(sub_arrays)
