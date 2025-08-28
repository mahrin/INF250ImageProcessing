# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:41:25 2021

@author: julie
"""
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import gaussian, median
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage.filters.rank import mean
from skimage.morphology import disk


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
    filename = 'UrStoy.tif'
    urstoy = plt.imread(filename)
    plt.title('Original')
    plt.imshow(urstoy, cmap='gray')
    
    # Histogram
    plt.figure()
    hist = histogram(urstoy)
    plt.plot(hist)
    
    # Histogram equalization
    eq_image = equalization(urstoy)
    plt.figure()
    plt.title('Histogram equalization')
    plt.imshow(eq_image, cmap='gray')

    hist_eq = histogram(eq_image)
    #plt.figure()
    #plt.plot(hist_eq)
    
    ## Filters
    # Gaussian
    urgauss = gaussian(urstoy)
    plt.figure()
    plt.title('Gaussian filter')
    plt.imshow(urgauss, cmap='gray')
    
    # Local mean
    urstoy = urstoy.copy()
    urmean = mean(urstoy, selem=disk(5))
    plt.figure()
    plt.title('Local mean filter')
    plt.imshow(urmean, cmap='gray')
    
    # Median
    urmedian = median(urstoy)
    plt.figure()
    plt.title('Median filter')
    plt.imshow(urmedian, cmap='gray')
    
    # Non-local mean
    urnlmean = denoise_nl_means(urstoy, preserve_range=False)
    plt.figure()
    plt.title('Non-local means filter')
    plt.imshow(urnlmean, cmap='gray')
    
    # Different sizes of filter windows?
    
    
    # Residual of each filter (with equalized not original)
    