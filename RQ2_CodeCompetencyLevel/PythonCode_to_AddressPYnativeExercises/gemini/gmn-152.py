import numpy as np

# Create the two NumPy arrays
arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])

# Add the two arrays
result = arrayOne + arrayTwo

# Print the addition result
print("Addition of two arrays is")
print(result)

# Calculate the square of each element in the result array
result_squared = np.square(result)

# Print the result after squaring
print("\nResult array after calculating the square root of all elements")
print(result_squared)
