# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:21:07 2021

@author: julie
"""

# -*- coding: utf-8 -*-

"""
INF250
Mandatory exercise 2
Julie Wollebæk Førrisdal
"""
import numpy as np
from skimage import filters
from skimage import feature


def edge_operator(image, operator):
    """Returns the result from one of the edge operators, prewitt, sobel,
    canny or laplace
    
    Parameters:
    -----------
    image : np.ndarray
        Image to detect blobs in. If this image is a colour image then 
        the last dimension will be the colour value (as RGB values).
    operator : numeric
    1 = sobel filter
    2 = prewitt filter
    3 = canny filter
    4 = laplace filter

    Returns:
    --------
    filtered : np.ndarray(np.uint)
    result image from the edge operator
    """    
    shape = np.shape(image)
    if len(shape) == 3:
        image = image.mean(axis=2)
        
    if operator == 1:
        filtered = filters.sobel(image)
    elif operator == 2:
        filtered = filters.prewitt(image)
    elif operator == 3:
        filtered = feature.canny(image)
    elif operator == 4:
        filtered = filters.laplace(image)
    else: 
        raise ValueError('Unvalid operator.')
    
    return filtered


def sharpen(image, sharpmask):
    """Performs an image sharpening using Laplace filter or unsharpen mask (USM)
    1 = Laplace
    2 = USM
    
    Returns: sharpened image
    """   
    shape = np.shape(image)
    if len(shape) == 3:
        image = image.mean(axis=2)
        
    if sharpmask == 1:
        image_lap = filters.laplace(image)  
        sharpened = image - 2*image_lap
    elif sharpmask == 2:
        gaussimage = filters.gaussian(image)
        sharpened = image + 2*(image-gaussimage)
    else:
        raise ValueError('Unvalid sharpmask.')
    return sharpened


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from skimage import io
    
    filename = 'AthenIR.png'
    athen = io.imread(filename)
    img = plt.imshow(athen, 'hot')
    plt.title('Original photo')
    plt.savefig('athen_original.png')
    plt.show()

    athen_sobel = edge_operator(athen, 1)
    img1 = plt.imshow(athen_sobel, 'hot')
    plt.title('Filter: Sobel')
    plt.savefig('athen_sobel.png')
    plt.show()
 
    athen_prewitt = edge_operator(athen, 2)
    img2 = plt.imshow(athen_prewitt, 'hot')
    plt.title('Filter: Prewitt')
    plt.savefig('athen_prewitt.png')
    plt.show()
    
    athen_canny = edge_operator(athen, 3)
    img3 = plt.imshow(athen_canny, 'hot')
    plt.title('Filter: Canny')
    plt.savefig('athen_canny.png')
    plt.show()
 
    athen_sharplaplace = sharpen(athen, 1)
    img5 = plt.imshow(athen_sharplaplace, 'hot')
    plt.title('Sharpened: Laplace')
    plt.savefig('athen_sharp_laplace.png')
    plt.show()
 
    athen_usm = sharpen(athen, 2)
    img6 = plt.imshow(athen_usm, 'hot')
    plt.title('Sharpened: USM')
    plt.savefig('athen_usm.png')
    plt.show()
