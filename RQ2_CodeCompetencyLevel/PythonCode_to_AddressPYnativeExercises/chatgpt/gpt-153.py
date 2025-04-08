import numpy as np

# Create an 8x3 array using numpy.arange
array = np.arange(10, 34).reshape(8, 3)

# Print the created array
print("Creating 8X3 array using numpy.arange")
print(array)

# Split the array into 4 equal-sized sub-arrays
sub_arrays = np.split(array, 4)

# Print the split sub-arrays
print("\nDividing 8X3 array into 4 sub arrays")
print(sub_arrays)
