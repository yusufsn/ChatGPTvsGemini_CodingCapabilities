import numpy as np

# Create the sample 2D array
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

# Print the original array
print("Printing Original array")
print(sampleArray)

# Find the minimum values along axis 1 (min in each row)
amin_axis1 = np.amin(sampleArray, axis=1)

# Print the result of amin on axis 1
print("\nPrinting amin Of Axis 1")
print(amin_axis1)

# Find the maximum values along axis 0 (max in each column)
amax_axis0 = np.amax(sampleArray, axis=0)

# Print the result of amax on axis 0
print("\nPrinting amax Of Axis 0")
print(amax_axis0)
