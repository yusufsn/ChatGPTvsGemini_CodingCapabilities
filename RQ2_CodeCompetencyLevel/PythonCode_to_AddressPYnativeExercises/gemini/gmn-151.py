import numpy as np

# Sample array
sampleArray = np.array([[3, 6, 9, 12],
                        [15, 18, 21, 24],
                        [27, 30, 33, 36],
                        [39, 42, 45, 48],
                        [51, 54, 57, 60]])

# Print the input array
print("Printing Input Array")
print(sampleArray)

# Select odd rows and even columns
result = sampleArray[1::2, 1::2]

# Print the result
print("\nPrinting array of odd rows and even columns")
print(result)
