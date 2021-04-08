from skimage import img_as_float, img_as_ubyte
from skimage.io import imread, imsave
import numpy as np
import warnings
warnings.simplefilter("ignore")


img = imread('img.png')
img = img_as_float(img)

r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]

r_mean, b_mean, g_mean = np.mean(r), np.mean(b), np.mean(g)
total_mean = (r_mean+b_mean+g_mean)/3

rw = r_mean / total_mean
bw = b_mean / total_mean
gw = g_mean / total_mean

r = r / rw
b = b / bw
g = g / gw

res = img.copy()

res[:,:,0] = r
res[:,:,1] = g
res[:,:,2] = b
res = np.clip(res, 0, 1)

imsave('out_img.png', img_as_ubyte(res))