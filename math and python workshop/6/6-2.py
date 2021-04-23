import numpy as np


V1 = np.fromstring(input(), sep=', ')
V2 = np.array(V1[-2])
V3 = V1[::-1]
V4 = V1[::3]
V5 = np.arange(V1.shape[0])

print(V1, V2, V3, V4, V5)


V1 = np.fromstring(input(), dtype=np.int, sep=', ')
V2 = np.fromstring(input(), dtype=np.int, sep=', ')
V3 = V1 + V2
V4 = V1[::2] * V2[::-2]

print(V1, V2, V3, V4)


V1 = np.fromstring(input(), sep=',')
V2 = np.fromstring(input(), sep=',')
V = V1[V1%V2[-2]==0] / V2[-2] 

print(V1, V2, V)

A1 = np.array((-1, 1))
A2 = np.array((2, 5))
A3 = np.array((5, -3))

print(abs(np.cross(A1-A2, A1-A3))/2)


M1 = np.array((
    (1., 2., 3., 0.),
    (4., 5., 6., 0.),
    (0., 1., 1., 6.),
    (7., 8., 9., 0.)
    ))

print(M1)
M1[-2] = np.sin(M1[-2]*np.pi/6)
print(M1)
M1[:,-2] = np.exp(M1[:,-2])
print(M1)

