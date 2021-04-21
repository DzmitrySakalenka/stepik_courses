import numpy as np
np.random.seed(42)

'''
Z = np.eye(int(input()))
print(Z)


Z = np.random.random_sample(list(map(int, input().split())))
print(Z)


Z = np.random.random_sample(list(map(int, input().split())))
print(Z.min(), Z.max(), sep='\n')


Z = np.random.random_sample(list(map(int, input().split())))
print(Z.mean())


Z = np.random.random_sample(list(map(int, input().split())))
X = Z.mean(axis=0)
print(X.min(), X.max(), sep='\n')


Z = np.ones(list(map(int, input().split())))
Z[1:-1,1:-1] = 0
print(Z)


Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)


Z = np.diag(1+np.arange(int(input())))
print(Z)


x, k = map(int, input().split())
print(x, k)
Z = np.diag(1+np.arange(k), k=x)
print(Z)


Z = np.zeros(list(map(int, input().split())))
Z[1::2,::2] = 1
Z[::2,1::2] = 1

Z = np.ones(list(map(int, input().split())))
Z[::2, ::2] = 0
Z[1::2,1::2] = 0

print(Z)
'''

i = 5
Z = np.array([[0, 1,  2,  3],
              [4, 5,  6,  7],
              [8, 9, 10, 11]])
print(np.unravel_index(i, Z.shape))
