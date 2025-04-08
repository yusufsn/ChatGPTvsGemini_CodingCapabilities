import numpy as np

# Given arrays
arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])

# Add the two arrays
result = arrayOne + arrayTwo

# Print the result of addition
print("Addition of two arrays is")
print(result)

# Square each element in the result array
result_squared = result ** 2

# Print the result array after squaring
print("\nResult array after calculating the square of all elements")
print(result_squared)
