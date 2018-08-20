# Generating random numbers
# You need to generate good quality random numbers

import numpy as np

np.random.seed(42) # fixed random numbers by seeding them
rand1 = np.random.geometric(p = 0.5, size=10)
rand2 = np.random.normal(50, 10, size=20)

rand3 = np.random.random()
#print(rand3)

np.mean(rand2)
np.median(rand2)
np.var(rand2)
np.std(rand2)