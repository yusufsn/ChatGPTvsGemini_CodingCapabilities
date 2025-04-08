import numpy as np
import matplotlib.pyplot as plt

# Create two 2-D arrays (example data)
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Create a figure and axis for plotting
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Plot the first 2-D array (array1) as a heatmap
ax[0].imshow(array1, cmap='viridis', interpolation='nearest')
ax[0].set_title('Array 1')
ax[0].colorbar()  # Display color bar

# Plot the second 2-D array (array2) as a heatmap
ax[1].imshow(array2, cmap='plasma', interpolation='nearest')
ax[1].set_title('Array 2')
ax[1].colorbar()  # Display color bar

# Show the plots
plt.tight_layout()
plt.show()
