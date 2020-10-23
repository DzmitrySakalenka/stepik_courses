from skimage.io import imread, imsave
import numpy as np


img = imread('img.png')
print(img.shape[1])


img = imread('img.png')
cpc = int(np.floor(float(img.shape[0])/2))
cpr = int(np.floor(float(img.shape[1])/2))
img[cpc, cpr, :] = [102, 204, 102]
imsave('out_img.png',img)


img = imread('img.png')
cpc = int(np.floor(float(img.shape[0])/2))
cpr = int(np.floor(float(img.shape[1])/2))
img[cpc-3:cpc+4, cpr-7:cpr+8, :] = [255, 192, 203]
imsave('out_img.png', img)


img = imread('img.png')

vertical_border = img[:,0]
horizontal_border = img[0,:]

left = 1
up = 1
right = 1
down = 1

while(np.array_equal(vertical_border, img[:, -1 + left])): left += 1
while(np.array_equal(vertical_border, img[:, 0 - right])): right += 1
while(np.array_equal(horizontal_border, img[-1 + up,:])): up += 1
while(np.array_equal(horizontal_border, img[0 - down,:])): down += 1
    
print('{} {} {} {}'.format(left-1, up-1, right-1, down-1))