import numpy as np

Z = np.random.randint(0, 10, (3, 3))
print("Original Matrix:\n", Z)

# Let's sort by the 2nd column (index 1)
n = 1
sorted_Z = Z[Z[:, n].argsort()]
print(f"Sorted by column {n}:\n", sorted_Z)