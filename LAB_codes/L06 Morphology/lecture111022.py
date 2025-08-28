#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:10:21 2019

@author: ingunn
"""

from skimage.morphology import skeletonize, dilation, opening, square
from skimage.morphology import erosion, closing
from skimage import data
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import numpy as np

from skimage.filters import threshold_otsu as otsu


from skimage.morphology import skeletonize, dilation, opening, square
from skimage.morphology import erosion, closing
from skimage import io

filename = 'rhino_detail.tif'

rhino = io.imread(filename)
plt.imshow(rhino,'gray')

rhinodil2 = dilation(rhinodil,square(3))
plt.figure()
plt.imshow(rhinodil2,'gray')



rhinoerode = erosion(rhinodil2,square(3))
plt.figure()
plt.imshow(rhinoerode,'gray')

rhinoerode2 = erosion(rhinoerode,square(3))
plt.figure()
plt.imshow(rhinoerode2,'gray')



rhinodilateerode = erosion(rhinodil,square(3))
plt.figure()
plt.imshow(rhinodilateerode,'gray')




filename = 'rhino_d.tif'

rhino = io.imread(filename)
plt.imshow(rhino,'gray')
rhinoclose = closing(rhino,square(7))
plt.figure()
plt.imshow(rhinoclose,'gray')

rhinoopen = opening(rhino,square(4))
plt.figure()
plt.imshow(rhinoopen,'gray')

rhinodilate2 = dilation(rhinoopen,square(3))
plt.figure()
plt.imshow(rhinodilate2,'gray')








bright_pixel = np.array([[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 1, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]], dtype=np.uint8)
plt.imshow(bright_pixel,'gray')
demodil = dilation(bright_pixel, square(3))

plt.imshow(demodil,'gray')


bright_pixel2 = np.array([[0, 0, 0, 0, 0],
                         [0, 1, 1, 1, 0],
                         [0, 1, 1, 1, 0],
                         [0, 1, 1, 1, 0],
                         [0, 0, 0, 0, 0]], dtype=np.uint8)
plt.figure()
plt.imshow(bright_pixel2,'gray')
demoerode = erosion(bright_pixel2, square(3))

plt.imshow(demoerode,'gray')

bad_connection = np.array([[1, 0, 0, 0, 1],
                            [1, 1, 0, 1, 1],
                            [1, 1, 1, 1, 1],
                            [1, 1, 0, 1, 1],
                            [1, 0, 0, 0, 1]], dtype=np.uint8)
plt.imshow(bad_connection,'gray')

demoe = erosion(bad_connection,square(3))
plt.figure()
plt.imshow(demoe,'gray')
demod = dilation(demoe, square(3))
plt.figure()
plt.imshow(demod,'gray')

demoopen = opening(bad_connection,square(3))
plt.figure()
plt.imshow(demoopen,'gray')


broken_line = np.array([[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [1, 1, 0, 1, 1],
                         [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]], dtype=np.uint8)

plt.imshow(broken_line,'gray')

demod = dilation(broken_line,square(3))
plt.imshow(demod,'gray')
demoe = erosion(broken_line, square(3))
plt.imshow(demoe,'gray')


democlose = closing(broken_line,square(3))
plt.figure()
plt.imshow(democlose,'gray')

# Invert the horse image
image = data.horse()
plt.imshow(image,'gray')

skeleton = skeletonize(image)
plt.imshow(skeleton,'gray')

imageinv = image
shape = np.shape(image)
for i in range(shape[0]):
    for j in range(shape[1]):
        if image[i,j] == 0:
            imageinv[i,j] = 1
        else:
            imageinv[i,j] = 0
            
plt.imshow(imageinv,'gray')

skeleton = skeletonize(imageinv)
plt.imshow(skeleton,'gray')
