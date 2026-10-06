import numpy as np

# Create a 16x16 array of ones (so every 4x4 block sum should exactly equal 16)
Z = np.ones((16, 16))

# Reshape into a 4x4 grid of 4x4 blocks, then sum the blocks
block_size = 4
block_sum = Z.reshape(16 // block_size, block_size, 16 // block_size, block_size).sum(axis=(1, 3))
print("Block Sums:\n", block_sum)