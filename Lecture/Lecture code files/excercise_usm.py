# -*- coding: utf-8 -*-

"""
Skeleton for excersize on edge operators
"""




def edge_operator(image, operator):
    """Returns the reusult from one of the edge operators, prewitt, sobel,
    canny eller laplace
    
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


    return filtered


def sharpen(image, sharpmask):
    """Performs an image sharpening using Laplace filter or unsharpen mask (USM)
    1 = Laplace
    2 = USM
    
    Returns: sharpened image
    """
    return sharpened


