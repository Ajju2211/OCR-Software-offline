#import matplotlib.pyplot as plt
from skimage import morphology
import numpy as np
import skimage

# read the image, grayscale it, binarize it, then remove small pixel clusters
im = plt.imread('original.jpeg')
grayscale = skimage.color.rgb2gray(im)
binarized = np.where(grayscale>0.1, 1, 0)
processed = morphology.remove_small_objects(binarized.astype(bool), min_size=2, connectivity=2).astype(int)

# black out pixels
mask_x, mask_y = np.where(processed == 0)
im[mask_x, mask_y, :3] = 0

# plot the result
#plt.figure(figsize=(10,10))
#plt.imshow(im)
