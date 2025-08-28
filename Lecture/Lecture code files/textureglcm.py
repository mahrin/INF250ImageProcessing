#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 09:56:26 2022

@author: ingunn
"""
import matplotlib.pyplot as plt

from skimage.feature import graycomatrix, graycoprops
from skimage import data
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte
import numpy as np

PATCH_SIZE = 21

# open the camera image
#image = data.camera()

#reading image
filename = 'cottage.tif'
from skimage import io
imagec = io.imread(filename)

imageg = rgb2gray(imagec)
image = img_as_ubyte(imageg)
# display image


plt.figure()
plt.imshow(image,cmap='gray')

# select some patches from grassy areas of the image
grass_locations = [(3757,301), (3500, 1000), (2248, 1240), (3135, 2690)]
grass_patches = []
for loc in grass_locations:
    grass_patches.append(image[loc[0]:loc[0] + PATCH_SIZE,
                               loc[1]:loc[1] + PATCH_SIZE])

# select some patches from sky areas of the image
sky_locations = [(600, 60), (1826, 355), (1575,2308), (604, 2340)]
sky_patches = []
for loc in sky_locations:
    sky_patches.append(image[loc[0]:loc[0] + PATCH_SIZE,
                             loc[1]:loc[1] + PATCH_SIZE])
    
 # select some patches from cottage areas of the image
cottage_locations = [(2971, 1032), (2960, 1522), (2850, 1250), (2960, 1675)]
cottage_patches = []
for loc in cottage_locations:
     cottage_patches.append(image[loc[0]:loc[0] + PATCH_SIZE,
                              loc[1]:loc[1] + PATCH_SIZE])   

# compute some GLCM properties each patch
xs = []
ys = []
for patch in (grass_patches + sky_patches + cottage_patches):
    glcm = graycomatrix(patch, distances=[5], angles=[0], levels=256,
                        symmetric=True, normed=True)
    xs.append(graycoprops(glcm, 'dissimilarity')[0, 0])
    ys.append(graycoprops(glcm, 'correlation')[0, 0])

# create the figure
fig = plt.figure(figsize=(8, 12))

# display original image with locations of patches
ax = fig.add_subplot(4, 2, 1)
ax.imshow(image, cmap=plt.cm.gray,
          vmin=0, vmax=255)
for (y, x) in grass_locations:
    ax.plot(x + PATCH_SIZE / 2, y + PATCH_SIZE / 2, 'gs')
for (y, x) in sky_locations:
    ax.plot(x + PATCH_SIZE / 2, y + PATCH_SIZE / 2, 'bs')
for (y, x) in cottage_locations:
    ax.plot(x + PATCH_SIZE / 2, y + PATCH_SIZE / 2, 'rs')    
ax.set_xlabel('Original Image')
ax.set_xticks([])
ax.set_yticks([])
ax.axis('image')

# for each patch, plot (dissimilarity, correlation)
ax = fig.add_subplot(4, 2, 2)
ax.plot(xs[:len(grass_patches)], ys[:len(grass_patches)], 'go',
        label='Grass')
ax.plot(xs[len(grass_patches):(len(grass_patches)+len(sky_patches))], ys[len(grass_patches):(len(grass_patches)+len(sky_patches))], 'bo',
        label='Sky')
ax.plot(xs[(len(grass_patches)+len(sky_patches)):], ys[(len(grass_patches)+len(sky_patches)):], 'ro',
        label='Cottage')
ax.set_xlabel('GLCM Dissimilarity')
ax.set_ylabel('GLCM Correlation')
ax.legend()

# display the image patches
for i, patch in enumerate(grass_patches):
    ax = fig.add_subplot(4, len(grass_patches), len(grass_patches)*1 + i + 1)
    ax.imshow(patch, cmap=plt.cm.gray,
              vmin=0, vmax=255)
    ax.set_xlabel(f"Grass {i + 1}")

for i, patch in enumerate(sky_patches):
    ax = fig.add_subplot(4, len(sky_patches), len(sky_patches)*2 + i + 1)
    ax.imshow(patch, cmap=plt.cm.gray,
              vmin=0, vmax=255)
    ax.set_xlabel(f"Sky {i + 1}")
    
for i, patch in enumerate(cottage_patches):
    ax = fig.add_subplot(4, len(cottage_patches), len(cottage_patches)*3 + i + 1)
    ax.imshow(patch, cmap=plt.cm.gray,
              vmin=0, vmax=255)
    ax.set_xlabel(f"Cottage {i + 1}")    



# display the patches and plot
fig.suptitle('Grey level co-occurrence matrix features', fontsize=14, y=1.05)
plt.tight_layout()
plt.show()