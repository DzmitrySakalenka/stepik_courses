import numpy as np

n = int(input())
a = np.zeros((n, n))

for i in range(n):
    a[i, :] = list(map(int, input().split()))

for i in range(n-1):
    c = a[i+1:, i] / a[i, i]
    a[i+1:, i:] -= c[np.newaxis].T * a[i, i:][np.newaxis]

print(a)
print(np.round(np.linalg.det(a)))