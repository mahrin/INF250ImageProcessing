# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 22:38:00 2021

@author: julie

Week 1 exercise 1

"""


from skimage.viewer import ImageViewer
from skimage import io
import matplotlib.pyplot as plt

# import and read
filename = 'fall.tiff'
fall = io.imread(filename)

# Display
plt.imshow(fall)

# Find shape
shape = fall.shape


# Find pixel RBG values 
a_red = fall[418, 356, 0]
a_green = fall[418, 356, 1]
a_blue = fall[418, 356, 2]

b_red = fall[550, 512, 0]
b_green = fall[550, 512, 1]
b_blue = fall[550, 512, 2]

c_red = fall[628, 844, 0]
c_green = fall[628, 844, 1]
c_blue = fall[628, 844, 2]


# Extracting each colour
red = fall[:,:,0]
green = fall[:,:,1]
blue = fall[:,:,2]

# Displaying each colour
plt.imshow(red, cmap='gray')
plt.imshow(green, cmap='gray')
plt.imshow(blue, cmap='gray')


# Minimum and maximum of each colour
r_min = min(red.flatten())
r_max = max(red.flatten())

g_min = min(green.flatten())
g_max = max(green.flatten())

b_min = min(blue.flatten())
b_max = max(blue.flatten())

# ALternative viewer
viewer = ImageViewer(fall)
viewer.show()



