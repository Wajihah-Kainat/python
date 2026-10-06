import numpy as np 

# Create a 5x5 array of random values
random_matrix = np.random.random((5, 5))
print("Matrix:\n", random_matrix)

# Find minimum and maximum
print("Minimum:", random_matrix.min())
print("Maximum:", random_matrix.max())