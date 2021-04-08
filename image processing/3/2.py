from skimage.io import imread, imsave
from numpy import dstack
import numpy as np
from skimage import img_as_float, img_as_ubyte
import warnings
warnings.simplefilter("ignore")


img = imread('img.png')
img = img_as_float(img)

r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]
y =  0.2126*r + 0.7152*g + 0.0722*b
u = -0.0999*r - 0.3360*g + 0.4360*b
v =  0.6150*r - 0.5586*g - 0.0563*b
k = round(y.size * 0.05)

extended_img = []

for pixel_row in y:
    for pixel in pixel_row:
        extended_img.append(pixel)

extended_img = np.array(extended_img)
extended_img.sort()

img_rescaled = extended_img[k:-k]

xmin = img_rescaled[0]
xmax = img_rescaled[-1]

y_contrast = (y - xmin) * (1 / (xmax - xmin))
y_rescaled = np.clip(y_contrast, 0, 1)

r = y_rescaled + 1.2803*v 
g = y_rescaled - 0.2148*u - 0.3805*v
b = y_rescaled + 2.1279*u

img_rgb = dstack((r, g, b))
img_rgb = np.clip(img_rgb, 0, 1)
img_rgb = img_as_ubyte(img_rgb)

imsave('out_img.png', img_rgb)