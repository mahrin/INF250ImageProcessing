#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 07:58:41 2017

@author: inbu
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import filters

from skimage import data, img_as_float
from skimage.data import astronaut
from skimage.color import rgb2gray

astro = rgb2gray(img_as_float(data.astronaut()))

plt.imshow(astro,'gray')

astro = astro[30:180,150:300]
plt.imshow(astro,'gray')

#sobel and prewitt filter
astro_sobel = filters.sobel(astro)
plt.imshow(astro_sobel,'gray')

astro_sobel_h = filters.sobel_h(astro)
plt.imshow(astro_sobel_h,'gray')

astro_sobel_v = filters.sobel_v(astro)
plt.imshow(astro_sobel_v,'gray')

astro_prewitt = filters.prewitt(astro)
plt.imshow(astro_prewitt,'gray')



from skimage import feature
edges1 = feature.canny(astro, sigma=1)
plt.imshow(edges1,'gray')

edges2 = feature.canny(astro, sigma=3)
plt.imshow(edges2,'gray')


edges2 = feature.canny(astro, sigma=1, low_threshold=0.15, high_threshold=0.3)
plt.figure()
plt.imshow(edges2,'gray')


# laplace filter
from skimage.filters import laplace
astro_lap = laplace(astro)
plt.imshow(astro_lap,'gray',vmin=0., vmax=0.2)
astro_sharp = astro-1*astro_lap
plt.imshow(astro_sharp, 'gray', vmin=0.4, vmax=0.9)


# high pass filter
from skimage.filters import gaussian
plt.imshow(astro,'gray')
gaussastro = gaussian(astro, sigma=5)
plt.imshow(gaussastro,'gray')
astro_high = astro-(gaussastro)
plt.imshow(astro_high,'gray', vmin=0., vmax=0.2)


# unsharpening mask to sharpen the image
amount = 2
usm_astro = astro + amount*(astro-gaussastro)
plt.imshow(usm_astro, 'gray', vmin=0.2, vmax=0.9)

plt.figure()
plt.imshow(astro,'gray', vmin=0.2, vmax=0.9)

plt.figure()
plt.hist(astro.ravel(),256,[0,1], color='black')
plt.show()



