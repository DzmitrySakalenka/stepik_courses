import numpy as np
import gauss as gs


def lsm(a):
    a = a.T
    n = a.shape[0]-1
    mat = np.zeros((n, n+1))

    for i in range(n):
        for j in range(n+1):
            mat[i, j] = sum(a[i, :]*a[j, :])

    tp, ans = gs.gauss(mat)
    
    if tp == 1:
        return ans
    
    return None


def pretty_lsm():
    n, m = map(int, input().split())
    a = np.zeros((n, m+1))

    for i in range(n):
        a[i, :] = list(map(int, input().split()))
    
    return ' '.join(map(str, lsm(a)))