import numpy as np

Z = np.random.uniform(0, 10, 5)
print("Original:", Z)

print("Method 1 (astype):", Z.astype(int))
print("Method 2 (trunc):", np.trunc(Z))
print("Method 3 (floor):", np.floor(Z))
print("Method 4 (modulo):", Z - Z % 1)
print("Method 5 (floor division):", Z // 1)