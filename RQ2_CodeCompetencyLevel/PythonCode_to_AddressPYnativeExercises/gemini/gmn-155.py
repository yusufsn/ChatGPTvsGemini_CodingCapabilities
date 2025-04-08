import numpy as np

# Create the sample array
sampleArray = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])

# Print the original array
print("Printing Original array")
print(sampleArray)

# Print the minimum along axis 1
print("\nPrinting amin Of Axis 1")
print(np.amin(sampleArray, axis=1))

# Print the maximum along axis 0
print("\nPrinting amax Of Axis 0")
print(np.amax(sampleArray, axis=0))
