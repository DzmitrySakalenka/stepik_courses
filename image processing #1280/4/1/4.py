from math import pi, e
import numpy as np
from skimage.io import imread, imsave
from skimage import img_as_float, img_as_ubyte
from scipy.signal import convolve2d
import warnings
warnings.filterwarnings("ignore")


def gaussian(x, y, sigma):
    return 1/((2*pi)*sigma**2)*e**((-x**2 - y**2)/(2*sigma**2))


img = imread('img.png')
img = img_as_float(img)
sigma = 0.66
k = round(3*sigma)
kernel = [[gaussian(x, y, sigma) for x in range(-k, k+1)] for y in range(-k, k+1)]
kernel = np.array(kernel)
norm_kernel = kernel / np.sum(kernel, axis=(0,1))
img = convolve2d(img, norm_kernel, mode='valid')
img = np.floor(img * 255)
img = np.ndarray.astype(img, np.uint8)
imsave('out_img.png', img)