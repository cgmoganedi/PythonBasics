import numpy as np

np.random.seed(41)
a = np.random.normal(25, 5, 100)
# np.histogram(a)
print(a)
print(np.histogram(a, 3))