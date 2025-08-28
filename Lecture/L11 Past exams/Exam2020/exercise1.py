#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:29:41 2017

@author: inbu
"""

import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import median
from skimage.filters import gaussian
from skimage.morphology import disk
from skimage import data, img_as_float
from skimage.color import rgb2gray
from skimage import io

from skimage.restoration import denoise_nl_means

filename = 'drone_blurr.tif'
drone1 = io.imread(filename)
plt.imshow(drone1)

drone = rgb2gray(drone1)
plt.imshow(drone,'gray')

gaussdrone = gaussian(drone, sigma=10)
plt.imshow(gaussdrone,'gray')



# unsharpening mask to sharpen the image
amount = 3
usm_drone = drone+ amount*(drone-gaussdrone)
plt.imshow(usm_drone, 'gray')

plt.figure()
plt.imshow(drone,'gray')


