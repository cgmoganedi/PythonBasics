from mpl_toolkits.mplot3d import axes3d
import matplotlib.plt as plt
import numpy as np

fig = plt.figure(5)
ax = fig.gca(projection='3d')

# axes range
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)

# axes labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# normalizing a matrix
def normalize(A):
    return A/np.linalg.norm(A)

# the vectors from the diagram
V = -normalize(np.array([1.0**0.5, 0.0**0.5, -1.0**0.5]))
L = np.array([0.5**0.5, 0.5**0.5, 0.0**0.5])
N = np.array([0.0**0.5, 0.5**0.5, 0.0**0.5])
R = np.array([-0.5**0.5, 0.0**0.5, 0.5**0.5])
#R = normalize(2*np.dot(N,L)*N-L)

vectors = [
    [[0.0, 0.0, 0.0], V],
    [[0.0, 0.0, 0.0], L],
    [[0.0, 0.0, 0.0], R],
    [[0.0, 0.0, 0.0], N],
]

colours = [
    (0, 0, 0, 1),
    (1, 0, 0, 1),
    (1, 0, 0, 1),
    (0, 0, 1, 1),
]

labels = [
    'V',
    'L',
    'R',
    'N'
]

#wtf is this loop doing
for i, vector in enumerate(vectors):
    x, y, z = vector[0]
    u, v, w = vector[1]
    ax.quiver(x, y, z, -u, -v, -w, length=1.0, arrow_length_ratio=0.0, colours=colours[i])
    ax.text(u, v, w, labels[i])
plt.show()

# ambient, defuse, specular and emission color components of the material
ma = np.array([0, 0, 0])
md = np.array([1, 0, 0])
ms = np.array([0, 0, 1])
me = np.array([0, 0, 0])

# ambient, defuse and specular light colour components
la = np.array([1, 1, 1])
ld = np.array([0.5, 0, 0])
ls = np.array([0, 0, 0.5])

# global ambient light
ga = np.array([0, 0, 0])

# hue
h = 0.5

# light equation
I = me + ga*ma + la*ma + ld*md*np.dot(L,N)+(
    ls*ms*np.max([0.0, np.dot(V,R)])
)**h

print(I)