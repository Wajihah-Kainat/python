import numpy as np

matrix = np.random.rand(3, 4)

# Keepdims=True ensures we can subtract the column mean from the rows
mean_subtracted = matrix - matrix.mean(axis=1, keepdims=True)
print("Mean Subtracted Matrix:\n", mean_subtracted)