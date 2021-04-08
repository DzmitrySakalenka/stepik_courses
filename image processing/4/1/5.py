from skimage.io import imread, imsave
import numpy as np
import warnings
warnings.filterwarnings("ignore")


img = imread('img.png')

kernel = np.array([[-1., -2., -1.],
                   [-2., 22., -2.],
                   [-1., -2., -1.]]) / 10
k_size = kernel.shape[0]
new_img = np.zeros((img.shape[0]-k_size+1, img.shape[1]-k_size+1))

for i in range(new_img.shape[0]):
    for j in range(new_img.shape[1]):
        new_img[i, j] = (img[i:(i+k_size),j:(j+k_size)] * kernel).sum().clip(0,255).astype('uint8')

new_img = new_img.astype('uint8')
imsave('out_img.png', new_img)