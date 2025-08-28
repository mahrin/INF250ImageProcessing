#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import matplotlib.pyplot as plt
import numpy as np

#reading image
filename = '../Images/fall.jpeg'
from skimage import io
fall = io.imread(filename)



# display image


plt.figure()
plt.imshow(fall)

# shape of image matrix
fall.shape

# extracting one colour and finding min and max values
fall_red = fall[:,:,0]

print(max(fall_red.flatten()))
print(min(fall_red.flatten()))

plt.imshow(fall_red,vmin=0,vmax=255,cmap='gray')
plt.show()


#mean av 3 RGB bilder
imagemean = fall.mean(axis=2)














