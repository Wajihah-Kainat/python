import numpy as np


def generate():
    yield from range(10)


# fromiter builds the array directly from the generator
gen_array = np.fromiter(generate(), dtype=int)
print("Generated Array:", gen_array)