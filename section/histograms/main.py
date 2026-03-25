import matplotlib.pyplot as plt
import numpy as np

size = 1000
normal_sample = np.random.normal(size=size)

# Create a probability density function approximation using a histogram
plt.hist(normal_sample,
         bins=1 + int(np.log2(size)),  # use 'size', not the array
         density=True)

plt.show()