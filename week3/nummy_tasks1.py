import numpy as np

# Create the vector (stops just before 50)
vector = np.arange(10, 50)
print("Original:\n", vector)

# Reverse it
reversed_vector = vector[::-1]
print("Reversed:\n", reversed_vector)