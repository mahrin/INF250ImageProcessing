#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 08:23:25 2018

@author: inbu
"""

from spectral import *
import numpy as np
import matplotlib.pyplot as plt
import skimage
import spectral.io.envi as envi

# import the image

img = envi.open('hyperspectral_vnir.hdr', 'hyperspectral_vnir.bsq')
wavelength = envi.read_envi_header('hyperspectral_vnir.hdr')['wavelength']
ww = [float(i) for i in wavelength]




imshow(img, (70, 50, 15), stretch=((0.02,0.98),(0.02,0.98),(0.02,0.98)))

hyperim = img[:,:,:]

blue = hyperim[:,:,10:20].mean(axis=2)
green = hyperim[:,:,40:50].mean(axis=2)
red = hyperim[:,:,65:75].mean(axis=2)

shape = hyperim.shape
rgb = np.zeros([shape[0],shape[1],3])
rgb[:,:,0]=red
rgb[:,:,1]=green
rgb[:,:,2]=blue
imshow(rgb,stretch=((0.02,0.98),(0.02,0.98),(0.02,0.98)))


# plotting spectra at selected points as fct of walvelength
#solar panel
z = np.array(hyperim[754,471,:].reshape(-1,1))
plt.figure()
plt.plot(ww,z)
#grass
z2 = np.array(img[600,390,:].reshape(-1,1))
plt.figure()
plt.plot(ww,z2)
#asphalt
z3 = np.array(img[724,235,:].reshape(-1,1))
plt.plot(ww,z3)
plt.show()
#water
z4 = np.array(img[470,946,:].reshape(-1,1))
plt.plot(ww,z3)
plt.show()

#plot as fct of pixel values
plt.figure()
plt.plot(z)
plt.show()

#compute mean spectrum of a region
#solar panel
m1 = hyperim[720:740,560:580,:].mean(axis=0)
m2 = m1.mean(axis=0).reshape(-1,1)
plt.figure()
plt.plot(ww,m2)
plt.show()
#grass
m1 = hyperim[570:590,370:390,:].mean(axis=0)
m2 = m1.mean(axis=0).reshape(-1,1)
plt.figure()
plt.plot(ww,m2)
plt.show()

#ndvi

ndvi_ima = (hyperim[:,:,108]-hyperim[:,:,94])/(hyperim[:,:,108]+hyperim[:,:,94])
plt.imshow(ndvi_ima,vmin=0,vmax=0.7)

# ndvi from spectral python
vi = ndvi(hyperim,94, 108)
plt.figure()
plt.imshow(vi,vmin=-0.3,vmax=0.6)

# pca
pc = principal_components(hyperim)
plt.figure()
plt.plot(pc.eigenvalues[0:10])
pc_0990 = pc.reduce(fraction=0.99)

# score images
img_pc = pc_0990.transform(hyperim)
plt.figure()
plt.imshow(img_pc[:,:,0], vmin=0.,vmax=0.05)
plt.figure()
plt.imshow(img_pc[:,:,1], vmin=0.,vmax=0.01)
plt.figure()
plt.imshow(img_pc[:,:,2], vmin=0,vmax=0.001)
plt.figure()
plt.imshow(img_pc[:,:,3], vmin=-0.1,vmax=0.15)
plt.figure()
plt.imshow(img_pc[:,:,4], vmin=-0.1,vmax=0.15)

# loadings
loadings = pc_0990.eigenvectors
plt.figure()
plt.plot(loadings[:,[2]])


# kmeans
(m,c) = kmeans(img_pc, 5, 30)
plt.imshow(m,'jet')
plt.figure()
for i in range(c.shape[0]):
    plt.plot(c[i])


# Gaussian Maximum Likelihood classification

#first creating ground truth image
shape = hyperim.shape
groundtruth = np.zeros([shape[0],shape[1]])

groundtruth[570:590,370:390] = 1.0   #grass
groundtruth[706:733,220:242] = 2.0 # asphalt
groundtruth[720:740,560:580] = 3.0 # solar panel
groundtruth[380:420,860:900] = 4.0 # water
groundtruth[600:625,580:610] = 5.0 # road2

plt.imshow(groundtruth)


# running the Gaussian Maximum Likelihood classification
classes = create_training_classes(hyperim, groundtruth)
gmlc = GaussianClassifier(classes)
clmap = gmlc.classify_image(hyperim)
imshow(classes=clmap)

