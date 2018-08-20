# Copying an array
import numpy as np
a = np.ones((6), dtype=int)

# no-copy sharing
# points to the same object  in memory
b = a

# shallow copy
ones1 = np.ones((3, 2), dtype=int)
view1 = ones1.view()

print(view1 is ones1)
print(view1.base is ones1)

view1.shape = 2,3

print(ones1)
print(view1)

# Deep copy
# Points to different objects
c = a.copy()

print(c is a)
print(c.base is a)

# Accessing array data
print(a)
a[1] = 2
a[3] = 7
print(a)

# Slicing an array
print(a[:3])

# Accessing one element in a matrix
print(ones1[1,0])

# Accessing a row
# Accessing a column
print(ones1)
print(ones1[1,:])
print(ones1[:,1])