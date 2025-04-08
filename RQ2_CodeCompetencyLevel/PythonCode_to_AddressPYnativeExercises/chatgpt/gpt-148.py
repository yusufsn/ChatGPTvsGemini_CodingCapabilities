import numpy as np

# Create a 4x2 array with unsigned int16 type
array = np.array([[64392, 31655], [32579, 0], [49248, 462], [0, 0]], dtype=np.uint16)

# Print the array
print("Printing Array\n")
print(array)

# Print the array attributes
print("\nPrinting NumPy array Attributes\n")
print(f"Array Shape is: {array.shape}")
print(f"Array dimensions are {array.ndim}")
print(f"Length of each element of array in bytes is {array.itemsize}")
