import numpy as np
# loading file into data objects

#data = np.loadtxt("./../0.0 - data/data.txt")
data = np.loadtxt("./../0.0 - data/data.txt", delimiter=',')

#data = np.load('mydata.npy')

# Saving the data onto a file
np.save("./../0.0 - data/mydata.npy", data)

np.savetxt("./../0.0 - data/mydata.csv", data, delimiter=',')

