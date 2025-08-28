#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:23:50 2017

@author: inbu
"""



import matplotlib.pyplot as plt
import numpy as np

#reading image
filename = '../Images/fall.tiff'
from skimage import io
fall = io.imread(filename)



# display image
plt.imshow(fall)

# shape of image matrix
fall.shape

# extracting one colour and finding min and max values
fall_red = fall[:,:,0]

print(max(fall_red.flatten()))
print(min(fall_red.flatten()))

plt.imshow(fall_red,vmin=0,vmax=255,cmap='gray')
plt.show()


#mean of 3 RGB bilder
imagemean = fall.mean(axis=2)
plt.imshow(imagemean,vmin=0,vmax=50,cmap='gray')
plt.show()



from skimage.color import rgb2gray
grayscaleima= rgb2gray(fall)
plt.imshow(grayscaleima,vmin=0,vmax=1,cmap='gray')
plt.show()

# histogram

histogram = np.zeros(256)
shape = np.shape(imagemean)
for i in range(shape[0]):
    for j in range(shape[1]):
        pixval = int(imagemean[i,j])
        histogram[pixval] += 1
plt.figure()        
plt.plot(histogram)



# function in python
plt.hist(imagemean.ravel(),256, [0,256], color='black'); plt.show()



# Binned histogram
K = 256
b = 32
histogram = np.zeros(b)
shape = np.shape(imagemean)
for i in range(shape[0]):
    for j in range(shape[1]):
        pixval = int(imagemean[i,j])
        histval = int(pixval*(b/K))
        histogram[histval] += 1
 
plt.figure()       
plt.plot(histogram)




# low contrast image
filename = '../Images/ireland.tif'
from skimage import io
ireland = io.imread(filename)
plt.imshow(ireland,cmap='gray')

histogram = np.zeros(256)
shape = np.shape(ireland)
for i in range(shape[0]):
    for j in range(shape[1]):
        pixval = int(ireland[i,j])
        histogram[pixval] += 1
plt.figure()        
plt.plot(histogram)


# Cumulated histogram

cumhist = np.zeros(256)
cumhist[0] = histogram[0]
for i in range(255):
    cumhist[i+1] = cumhist[i] + histogram[i+1]

plt.figure()    
plt.plot(cumhist)







# histogram equalisation
M = shape[0]
N = shape[1]
for i in range(shape[0]):
    for j in range(shape[1]):
        a = int(ireland[i,j])
        b = cumhist[a]*(K-1)/(M*N)
        ireland[i,j] = b
        
plt.imshow(ireland,'gray')
plt.figure()
plt.hist(ireland.ravel(),256,[0,256])
plt.show()




# Point operations 

# increasing contrast with 50 %
plt.imshow(imagemean,cmap='gray') 
shape = np.shape(imagemean)
for i in range(shape[0]):
    for j in range(shape[1]):
        imagemean[i,j] = int(imagemean[i,j]*1.5+0.5)
        if imagemean[i,j] > 255:
            imagemean[i,j] = 255
plt.imshow(imagemean,cmap='gray')            
            
# Inversion
            
maxval = max(imagemean.flatten())
for i in range(shape[0]):
    for j in range(shape[1]):
        imagemean[i,j] = int(-imagemean[i,j] + maxval)
            
plt.imshow(imagemean,cmap='gray')    
