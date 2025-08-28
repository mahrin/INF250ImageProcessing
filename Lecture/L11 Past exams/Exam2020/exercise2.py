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
from skimage.exposure import equalize_hist

#string fault

#reading image
filename = 'string.jpg'
from skimage import io
pv1 = io.imread(filename)
filename = 'module.tif'
pv2 = io.imread(filename)

plt.figure()
plt.imshow(pv1[:,:,0],'gray')
plt.figure()
plt.imshow(pv1[:,:,1],'gray')
plt.figure()
plt.imshow(pv1[:,:,2],'gray')


plt.figure()
plt.imshow(pv2[:,:,0],'gray')
plt.figure()
plt.imshow(pv2[:,:,1],'gray')
plt.figure()
plt.imshow(pv2[:,:,2],'gray')

#selecting the band with the most signal
pv1g = pv1[50:450,100:500,2]

pv2g = pv2[100:400,100:500,2]


plt.figure()
plt.imshow(pv1g,'gray')
plt.figure()
plt.imshow(pv2g,'gray')




pv2eq = equalize_hist(pv2g)

plt.figure()
plt.imshow(pv2eq,'gray')

#plt.figure()
#plt.imshow(pv2g,'gray')

# display image
#plt.imshow(pv2g,cmap='gray')
#plt.figure()
#plt.hist(pv1g.ravel(),256, [0,256], color='black'); plt.show()

radius = 15
selem = disk(radius)

local_otsu = rank.otsu(pv2g, selem)


threshold_global_otsu = threshold_otsu(pv2g)
global_otsu = pv2g >= threshold_global_otsu

plt.figure()
plt.imshow(pv2g>= local_otsu, cmap='gray')
plt.figure()
plt.imshow(global_otsu, cmap='gray')


threshold_global_otsu = threshold_otsu(pv1g)
global_otsu = pv1g >= threshold_global_otsu
plt.figure()
plt.imshow(global_otsu, cmap='gray')
#module fault










   
