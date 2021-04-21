import numpy as np


print(np.__version__)


n = int(input())
Z = np.zeros(n)
print(Z)


params = input().split()
t = 'float64' if params[-1].isdigit() else params.pop()
Z = np.zeros(tuple(map(int, params)), dtype=t)
print(Z)


Z = np.zeros((10,10))
print(Z.size * Z.itemsize)


np.info(np.add)
np.info(np.array)


Z = np.zeros(int(input()))
Z[int(input())] = 1
print(Z)


Z = np.arange(int(input()), int(input()) + 1)


Z = np.arange(50)
Z = Z[::-1]
print(Z)


Z = np.arange(int(input())).reshape(list(map(int, input().split())))
print(Z)


Z = np.array([1, 0, 2, 0, 3, 0, 4])
NonZerros = np.nonzero(Z)
print(NonZerros)


Z = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [0, 0, 9]])

print(list(Z[Z>3]))

