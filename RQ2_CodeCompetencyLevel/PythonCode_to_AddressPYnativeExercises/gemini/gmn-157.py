import numpy as np
import matplotlib.pyplot as plt

# Create two 2D arrays
array1 = np.random.rand(5, 5)
array2 = np.random.randint(1, 10, size=(5, 5))

# Plot the first array as a heatmap
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(array1, cmap='coolwarm')
plt.title('Heatmap of Array 1')
plt.colorbar()

# Plot the second array as a bar chart
plt.subplot(1, 2, 2)
plt.bar(range(5), array2.mean(axis=1))
plt.title('Average Values of Rows in Array 2')
plt.xlabel('Row Index')
plt.ylabel('Average Value')

plt.tight_layout()
plt.show()
