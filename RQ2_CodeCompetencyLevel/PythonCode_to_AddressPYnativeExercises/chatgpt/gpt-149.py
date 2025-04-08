import numpy as np

# Create an array from 100 to 200 with a step of 10
array = np.arange(100, 200, 10)

# Reshape the array to 5x2
array_reshaped = array.reshape(5, 2)

# Print the array
print("Creating 5X2 array using numpy.arange")
print(array_reshaped)
