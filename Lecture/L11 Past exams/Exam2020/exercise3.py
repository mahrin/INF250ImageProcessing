#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:23:50 2017

@author: inbu
"""



import matplotlib.pyplot as plt
import numpy as np
from skimage.morphology import disk
from skimage.filters import threshold_otsu, rank
from skimage import exposure
from skimage.color import rgb2gray



#reading image
filename = 'UVfluorim.tif'
from skimage import io
pv1 = io.imread(filename)

# display image
plt.figure()
plt.imshow(pv1)

#selecting the band with the most signal
pv1g = pv1[:,:,2]



# display image
plt.figure()
plt.imshow(pv1g,cmap='gray')



# histogram

histogram = np.zeros(256)
shape = np.shape(pv1g)
for i in range(shape[0]):
    for j in range(shape[1]):
        pixval = int(pv1g[i,j])
        histogram[pixval] += 1
plt.figure()        
plt.plot(histogram)


#histogram equalisation
# Cumulated histogram

cumhist = np.zeros(256)
cumhist[0] = histogram[0]
for i in range(255):
    cumhist[i+1] = cumhist[i] + histogram[i+1]

plt.figure()    
plt.plot(cumhist)

# histogram equalisation
pv2 = pv1g
K = 256
M = shape[0]
N = shape[1]
for i in range(shape[0]):
    for j in range(shape[1]):
        a = int(pv2[i,j])
        b = cumhist[a]*(K-1)/(M*N)
        pv2[i,j] = b
        
plt.imshow(pv2,'gray')
plt.figure()
plt.hist(pv2.ravel(),256,[0,256])
plt.show()



# trehshold with Otsu

radius = 35
selem = disk(radius)

local_otsu = rank.otsu(pv1g, selem)
plt.figure()
plt.imshow(pv1g>= local_otsu, cmap='gray')



threshold_global_otsu = threshold_otsu(pv2)

global_otsu = pv2 >= threshold_global_otsu


plt.figure()
plt.imshow(global_otsu, cmap='gray')









   
