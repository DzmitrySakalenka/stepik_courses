from decimal import *
import numpy as np
getcontext().prec = 50


def luka(L0, L1, n):
    for _ in range(n):
        L0, L1 = L1, L0 + L1
    return L0


def fi(L0, L1, n):
    for _ in range(n-1):
        L0, L1 = L1, L0 + L1
    return Decimal(L1) / Decimal(L0)


def super_L(n):
    return np.linalg.matrix_power(np.array([[0, 1], [1, 1]], 'O'), n).dot([2, 1])[0] if n else 2


print(luka(42, 13, 0))
print(luka(12345, 67890, 5))
print(luka(0, 1, 6))

print(fi(0, 1, 11))


print(super_L(5**1 * 3**2 * 2**2))
print(super_L(5**4 * 3**4 * 2**4))
print(super_L(3**10))