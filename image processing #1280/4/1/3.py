from math import pi, e
import numpy as np


def gaussian(x, y, sigma):
    return 1/((2*pi)*sigma**2)*e**((-x**2 - y**2)/(2*sigma**2))


sigma = float(input())
k = round(3*sigma)
kernel = [[gaussian(x, y, sigma) for x in range(-k, k+1)] for y in range(-k, k+1)]
kernel = np.array(kernel)
norm_kernel = kernel / np.sum(kernel, axis=(0,1))
print('\n'.join([' '.join(['{:.5f}'.format(item) for item in row]) for row in norm_kernel]))