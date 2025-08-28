# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 15:07:55 2021

@author: julie
"""

import matplotlib.pyplot as plt
import numpy as np


def histogram(image):
    """Returns the image histogram with 256 bins.
    """
    # Setup
    shape = np.shape(image)
    histogram = np.zeros(256)
    
    # Histogram
    for x in range(shape[0]):
        for y in range(shape[1]):
            # Find intensity value
            pixel_value = int(image[x, y])
            # Update histogram by counting intensity value
            histogram[pixel_value] += 1 
    return histogram


def contrast(image, contrast):
    """Change contrast of image (point operation).
    """
    shape = np.shape(image)
    new_image = np.zeros_like(image)
    
    #Loop through pixels one by one:
    for x in range(shape[0]):
        for y in range(shape[1]):
            # Change contrast:
            new_image[x, y] = int(image[x, y] * contrast)
            
            # Max value is 255:
            if new_image[x, y] > 255:
                new_image[x, y] = 255
    return new_image


def brightness(image, brightness):
    """Change brightness of image (by point operation).
    """
    shape = np.shape(image)
    new_image = np.zeros_like(image)
    
    #Loop through pixels one by one:
    for x in range(shape[0]):
        for y in range(shape[1]):
            # Change brightness:
            new_image[x, y] = int(image[x, y] + brightness)
            # Max value is 255:
            if new_image[x, y] > 255:
                new_image[x, y] = 255

    return new_image


def cumulative_hist(image):
    cumulhist = np.zeros(256)
    hist = histogram(image)
    cumulhist[0] = hist[0]
    
    for i in range(255):
        cumulhist[i+1] = cumulhist[i] + hist[i+1]
    
    return cumulhist


def equalization(image):
    shape = np.shape(image)
    cumulhist = cumulative_hist(image)
    new_image = np.zeros_like(image)
    M = shape[0]
    N = shape[1]
    K = 256

    for i in range(shape[0]):
        for j in range(shape[1]):
            a = int(image[i,j])
            b = cumulhist[a]*(K-1)/(M*N)
            new_image[i,j] = b
    return new_image
    

if __name__ == '__main__':
    # Read and display image
    filename = 'airfield.tif'
    airfield = plt.imread(filename)
    airfield = airfield.astype('float64')
    plt.imshow(airfield, cmap='gray')
    
    # Make histogram
    hist = histogram(airfield)
    plt.figure()
    plt.plot(hist)
    
    # Increase contrast by 50%:
    image50 = contrast(airfield, 1.5)
    plt.figure()
    plt.imshow(image50, cmap='gray')

    # Change brightness by +10:
    image10 = brightness(airfield, 10)
    plt.figure()
    plt.imshow(image10, cmap='gray')
    
    # Histogram equalization
    eq_image = equalization(airfield)
    plt.figure()
    plt.imshow(eq_image, cmap='gray')
 
    hist_eq = histogram(eq_image)
    plt.figure()
    plt.plot(hist_eq)
    
    # Otsu threshold
    from skimage.filters import threshold_otsu
    thresh = threshold_otsu(airfield)
    binary = airfield > thresh
    plt.figure()
    plt.imshow(binary, cmap='gray')
    

        
    
