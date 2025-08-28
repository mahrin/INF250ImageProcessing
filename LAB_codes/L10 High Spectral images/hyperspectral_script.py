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

hyperim = np.load("Oslo_hsi.npy")
wavelength = envi.read_envi_header('Visnir.hdr')['wavelength']
ww = [float(i) for i in wavelength]



imshow(hyperim, (10, 48, 70), stretch=((0.02,0.98),(0.02,0.98),(0.02,0.98)))



#np.save("Oslo_hsi.npy",hyperim)

# plotting spectra at selected points as fct of walvelength

z = np.array(hyperim[521,520,:].reshape(-1,1))
z2 = np.array(hyperim[635,214,:].reshape(-1,1))
z3 = np.array(hyperim[441,36,:].reshape(-1,1))
plt.figure()
plt.plot(ww,z)
plt.plot(ww,z2)
plt.plot(ww,z3)
plt.show()

#plot as fct of pixel values
plt.figure()
plt.plot(z)
plt.show()

#compute mean of all spectra
m1 = hyperim.mean(axis=0)
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
pc_0999 = pc.reduce(fraction=0.999)

# score images
img_pc = pc_0999.transform(hyperim)
plt.figure()
plt.imshow(img_pc[:,:,0], vmin=-0.1,vmax=0.15)
plt.figure()
plt.imshow(img_pc[:,:,1], vmin=-0.1,vmax=0.15)
plt.figure()
plt.imshow(img_pc[:,:,2], vmin=-0.1,vmax=0.15)
plt.figure()
plt.imshow(img_pc[:,:,3], vmin=-0.1,vmax=0.15)
plt.figure()
plt.imshow(img_pc[:,:,4], vmin=-0.1,vmax=0.15)





# loadings
loadings = pc_0999.eigenvectors
plt.figure()
plt.plot(loadings[:,[0,1,2,3,4]])

# kmeans
(m,c) = kmeans(img_pc, 5, 30)
plt.imshow(m,'jet')
plt.figure()
for i in range(c.shape[0]):
    plt.plot(c[i])


shape = hyperim.shape
groundtruth = np.zeros([shape[0],shape[1]])

groundtruth[128:168,336:366] = 1.0   #grass
groundtruth[623:650, 200:250] = 2.0 # asphalt
groundtruth[460:480, 150:170] = 3.0 # roof1

groundtruth[350:370, 300:320] = 3.0 # roof1

plt.figure()
plt.imshow(groundtruth)

# Gaussian Maximum Likelihood classification

classes = create_training_classes(hyperim, groundtruth)
gmlc = GaussianClassifier(classes)
clmap = gmlc.classify_image(hyperim)
plt.figure()
imshow(classes=clmap)

