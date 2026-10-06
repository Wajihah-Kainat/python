import numpy as np

# Create random matrices
A = np.random.random((5, 3))
B = np.random.random((3, 2))

# Multiply them
C = np.dot(A, B)
print("Matrix Product:\n", C)