import numpy as np

matrix = np.random.random((5, 5))

# Normalize the matrix using standard Min-Max scaling
normalized_matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min())
print("Normalized Matrix:\n", normalized_matrix)