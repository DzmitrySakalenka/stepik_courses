import numpy as np
np.random.seed(42)


Y = np.array([[99, 11, 55],
              [33, 66, 99]])
Z = np.round((Y - np.mean (Y)) / (np.std (Y)), 2)
print(Z)


A = np.array([1.5, 2.5, 3.5])
B = np.array([4, 5, 6])
Z = A @ B
print(Z)


A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[11.5],
              [12.5],
              [13.5]])
Z = A @ B
print(Z)

A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[11.5, 12.5, 13.5]])
try:
    Z = A @ B
except ValueError:
    Z = 'Упс! Что-то пошло не так...'
print(Z)


Z = np.arange(11)
Z[(3 < Z) & (Z < 9)] *= -1
print(Z)


A = np.array([-3.1, -5.9, 0, 2.2, 9.8])
Z = np.copysign(np.ceil(np.abs(A)), A)
print(Z)
Z = np.where(A>0, np.ceil(A), np.floor(A))
print(Z)


A = np.array([0, 9, 7, 1, 3, 7, 5, 2, 5, 1])
B = np.array([3, 1, 3, 7, 4, 1, 8, 1, 1, 8])
Z = np.intersect1d(A, B)
print(Z)