from skimage.io import imread, imsave
import numpy as np


img = imread('img.png')
img = (img - img.min()) * (255 / (img.max() - img.min()))
imsave('out_img.png', img.astype('uint8'))


img = imread('img.png')
k = round(img.size * 0.05)
x = sorted(img.flatten())
x1 = x[k:((img.size - 1) - k)]
print(min(x1), max(x1))


img = imread('img.png')
k = round(img.size * 0.05)
x = sorted(img.flatten())[k:((img.size - 1) - k)]
img = np.clip(img, min(x), max(x))
img = (img - min(x)) * (255 / (max(x) - min(x)))
imsave('out_img.png', img.astype(np.uint8))