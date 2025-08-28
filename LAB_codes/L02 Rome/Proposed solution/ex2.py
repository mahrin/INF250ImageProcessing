"""
by Joel Yacob Teklemariam
"""

from skimage.filters._gaussian import gaussian
from skimage import io
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
from skimage import color

## Gaussian, sigma = 5

bilde_navn = "gingerbreads.jpg"
bilde = io.imread(bilde_navn)

plt.imshow(bilde)
plt.show()

filter_fountain = gaussian(bilde, sigma=5)
plt.imshow(filter_fountain)
plt.show()


## Threshold otsu

bilde_to_gray = color.rgb2gray(bilde)

## kopiert fra link til oppgaven
## med justeringer.
thresh = threshold_otsu(bilde_to_gray)
binary = bilde_to_gray > thresh

fig, axes = plt.subplots(ncols=3, figsize=(8, 3))
ax = axes.ravel()
ax[0] = plt.subplot(1, 3, 1)
ax[1] = plt.subplot(1, 3, 2)
ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0])

ax[0].imshow(bilde, cmap=plt.cm.gray)
ax[0].set_title('Original')
ax[0].axis('off')

ax[1].imshow(bilde_to_gray, cmap=plt.cm.gray)
ax[1].set_title('Original grayscale')
ax[1].axis('off')

# ax[1].hist(bilde_to_gray.ravel(), bins=256)
# ax[1].set_title('Histogram')
# ax[1].axvline(thresh, color='r')

ax[2].imshow(binary, cmap=plt.cm.gray)
ax[2].set_title('Thresholded')
ax[2].axis('off')

plt.show()