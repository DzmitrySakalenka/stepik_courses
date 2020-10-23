from skimage.io import imread, imsave
import numpy as np
import warnings
warnings.filterwarnings("ignore")


img = imread('img.png')

k_size = 7
new_img = np.zeros((img.shape[0]-k_size+1, img.shape[1]-k_size+1))

for i in range(new_img.shape[0]):
    for j in range(new_img.shape[1]):
        new_img[i, j] = np.median(img[i:(i+k_size),j:(j+k_size)])

new_img = new_img.astype('uint8')
imsave('out_img.png', new_img)