from skimage import img_as_ubyte
from skimage.io import imread, imsave
import numpy as np


img = imread('img.png')
img = img_as_ubyte(img)
h = np.zeros(256, np.uint32)

for v in img.flatten():
    h[v] += 1  

cdf = np.zeros(256, np.uint32)

for v in range(256):
    cdf[v] = cdf[v-1] + h[v]  

min_sum = 99999

for val in cdf:
    if val != 0 and val < min_sum:
        min_sum = val  

p = len(img.flatten())
res = img.copy()

for y in range(img.shape[0]):
    for x in range (img.shape[1]):
        pixel = img[y][x]
        res[y][x] = round((cdf[pixel]-min_sum)/(p-1)*255)

imsave('out_img.png', res)