import numpy as np

# a vector
a = np.array(
    [1.0, 2.0]
)

# 2 by 2 matrix
b = np.array([
    [1.0, 2.0],
    [3.0, 4.0]
])
# 3 by 3 matrix
c = np.array([
    [1.0, 2.0],
    [3.0, 4.0],
    [5.0, 6.0]
])

# Fast Fourier Transforms
print(np.fft.fft(a)) # for 1 dimensional array or vector
print(np.fft.fft2(b)) # for 2 dimensional array or matrix
print(np.fft.fftn(c)) # for 3 or more dimensional matrix
print(np.fft.fft(c, axis=0)) # use n by m in a 1 dimensional fft