import numpy as np

# Create a 4x2 integer array with unsigned int16 data type
array = np.array([[64392, 31655],
                  [32579, 0],
                  [49248, 462],
                  [0, 0]], dtype=np.uint16)

# Print the array
print("Printing Array")
print(array)

# Print array attributes
print("\nPrinting NumPy array Attributes")
print("Array Shape is:", array.shape)
print("Array dimensions are:", array.ndim)
print("Length of each element of array in bytes is:", array.itemsize)
