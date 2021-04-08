from skimage.io import imread, imsave
from numpy import ones
from scipy.signal import convolve2d
import warnings


warnings.filterwarnings("ignore")
img = imread('img.png')
img = convolve2d(img, ones((5, 5), dtype=int), mode='valid') // 25
imsave('out_img.png', img)