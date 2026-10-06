import numpy as np

# 5 points, 2 coordinates (x, y)
coords = np.random.random((5, 2))

# Using broadcasting to calculate the distance formula: sqrt((x2-x1)^2 + (y2-y1)^2)
X, Y = np.atleast_2d(coords[:, 0], coords[:, 1])
distances = np.sqrt((X - X.T)**2 + (Y - Y.T)**2)
print("Distances:\n", distances)