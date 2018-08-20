import numpy as np

# 2 by 2 matrix
a = np.array([
    [1.0, 2.0],
    [ 3.0,4.0]
])

# get the inverse of a matrix
print(np.linalg.inv(a))

# get the norm of a matrix
print(np.linalg.norm(a))

# get the trace of a matrix
# this is a method the array object
print(a.trace())

# get the transpose of a matrix
# this is also a method of the matrix object
print(a.transpose())