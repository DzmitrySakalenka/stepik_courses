from numpy import dstack
from skimage.io import imread, imsave
from skimage import img_as_float, img_as_ubyte


img = imread('img.png')
img = img.max() - img
imsave('out_img.png', img)


img = imread('img.png')
imsave('out_img.png', dstack((img[:,:,2], img[:,:,0], img[:,:,1])))


img = imread('img.png')
img = img_as_float(img)
img = img_as_ubyte(0.2126*img[:,:,0] + 0.7152*img[:,:,1]+0.0722*img[:,:,2])
imsave('out_img.png', img)