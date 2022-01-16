import multiprocessing as mp
print("Number of processors: ", mp.cpu_count())
import numpy as np
from time import time

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[15, 5])
data = arr.tolist()
data[:5]
print(data[:5])