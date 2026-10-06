import numpy as np

A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)

# array_equal returns True only if shapes and elements match exactly
is_equal = np.array_equal(A, B)
print(f"Array A: {A}, Array B: {B}")
print("Are they equal?", is_equal)