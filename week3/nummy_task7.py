import numpy as np

# Define the structure (data types) for the array
structured_array = np.zeros(5, [('position', [('x', float), ('y', float)]),
                                ('color',    [('r', int), ('g', int), ('b', int)])])
print("Structured Array:\n", structured_array)