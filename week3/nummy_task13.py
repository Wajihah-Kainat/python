import numpy as np

Z = np.random.uniform(0, 1, (5, 5))
rank = np.linalg.matrix_rank(Z)
print("Matrix Rank:", rank)