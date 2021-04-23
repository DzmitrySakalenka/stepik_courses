import numpy as np
np.random.seed(42)


defaults = np.seterr(all="ignore")
Z = np.ones(1) / 0

_ = np.seterr(**defaults)


np.sqrt(-1) == np.emath.sqrt(-1)


Z = np.arange(input(), input(), dtype='datetime64[D]')
print(Z)


Z = np.random.uniform(0,10,10)
print(Z - Z%1)
print(np.floor(Z))
print(np.ceil(Z)-1)
print(Z.astype(int))
print(np.trunc(Z))


n, m = map(int, input().split())
k = float(input())
Z = np.tile(np.arange(k,k+m), (n, 1))
print(Z)


n, m = map(int, input().split())
k = float(input())
Z = np.tile(np.arange(k,k+n), (m, 1)).T
print(Z)


V = range(10)
Z = np.fromiter(V, dtype=float, count=-1)
print(Z)


Z = np.round(np.linspace(int(input()), int(input()), num=int(input())+2)[1:-1], 3)
print(Z)


Z = np.geomspace(int(input()), int(input()), num=int(input()))
print(Z)


np.random.seed(int(input()))
Z = np.random.rand(int(input()))
Z.sort()
