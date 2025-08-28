# Importing all the necessary modules
from spectral import *
import numpy as np
import matplotlib.pyplot as plt
import skimage
import math


hyperim = np.load("sandvika.npy")

# Function for finding the required bands
def find_bands(all_wavelengths,required_wavelengths):
    required_bands = {}
    
    for wavelength in required_wavelengths.keys():
            min_distance = None
            min_wave_val = None
            band = None
            for index, wave_val in enumerate(all_wavelengths): 
                current_distance = abs(wavelength - wave_val)
                if min_distance == None:
                    min_distance = current_distance
                    min_wave_val = wave_val
                    band = index+1
                elif current_distance> min_distance:
                    break
                elif current_distance< min_distance:
                    min_distance = current_distance
                    min_wave_val = wave_val
                    band = index +1    

            band_name = required_wavelengths[wavelength]
            required_bands[band_name]=band        
    return required_bands

# Calling the function to get required wavelength bands
wavelength = envi.read_envi_header('Visnir.hdr')['wavelength']
all_wavelengths = [float(i) for i in wavelength]
required_wavelengths = {440:"blue", 535:'green', 645:'red', 800:'NIR'}
required_bands = find_bands(all_wavelengths, required_wavelengths)
print("required_bands", required_bands)


#Organising the RGB bands in list format
print("required_bands", required_bands)   
RGB_bands = [required_bands['red'],required_bands['green'],required_bands['blue']]
print("RGB_bands", RGB_bands)
NIR_band = required_bands['NIR']
print("NIR_band", NIR_band)
red_band = required_bands['red']
print("red_band", red_band)


imshow(hyperim, bands = RGB_bands, stretch=((0.02,0.98),(0.02,0.98),(0.02,0.98)), figsize=(12,8))
plt.title("RGB image with 1 band for each color")
plt.show()



np.seterr(invalid='ignore') #ignoring the Nan values
ndvi_image_manual = (hyperim[:,:,NIR_band]-hyperim[:,:,red_band])/(hyperim[:,:,NIR_band]+hyperim[:,:,red_band])

# NDVI image calculated using equation
plt.figure(figsize=(10,8))
plt.imshow(ndvi_image_manual,vmin=0.1,vmax=0.9, cmap='RdYlGn') 
plt.title("NDVI image calculated using equation")
plt.show()




# Generating PCA plot to explain the variance present in the image
pc = principal_components(hyperim)
plt.figure(figsize=(8,5))
plt.plot(pc.eigenvalues[0:10])
plt.title("PCA plot")
plt.xlabel('Nnumber of Component (PCAs)')
plt.ylabel('Explained variance [%]')
plt.show()

# PCA iamge calculation
pc_0994 = pc.reduce(fraction=0.994)# select the PC with 99.4% variance-
img_pc = pc_0994.transform(hyperim) # then transforming that PC with 99.4% to our original image
print("Number of PCA's selected", img_pc.shape[2])
imshow(img_pc, stretch=((0.02,0.98),(0.02,0.98),(0.02,0.98)), figsize=(10,8), title ='PCA image')
plt.show()




fig, ax = plt.subplots(nrows = 1, ncols = 3, figsize = (14, 7))
ax[0].imshow(img_pc[:,:,0], vmin=-22000,vmax=10000)
ax[0].set_title(r'PC0 image', fontsize = 13)

ax[1].imshow(img_pc[:,:,1], vmin=-7500,vmax=4000)
ax[1].set_title(r'PC1 image', fontsize = 13)

ax[2].imshow(img_pc[:,:,2], vmin=-500,vmax=1000)
ax[2].set_title(r'PC2 image', fontsize = 13)


for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()




# loadings
loadings = pc_0994.eigenvectors 

#plotting the graph
fig, ax_dict = plt.subplot_mosaic([ ['bottom', 'BLANK']], empty_sentinel="BLANK", figsize = (20, 5))

ax_dict['bottom'].plot( loadings[:,[0]], color = 'g', label='PC0 (Vegetation)')
ax_dict['bottom'].plot( loadings[:,[1]], color = 'r', label='PC1 (Roofs and roads)')
ax_dict['bottom'].plot( loadings[:,[2]], color = 'b', label='PC2 (small details and shadows present)')
# Place a legend to the right of this smaller subplot.
ax_dict['bottom'].legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)


plt.title('Loading plot')
plt.xlabel('Band number')
# plt.ylabel("Pixel count")
plt.show()



# For stopping the spectral information printing
import logging, sys
logging.disable(sys.maxsize)



#Function for calculating the clusters and displaying the result images
def k_means_analysis(image, cluster_number, vmin, vmax):
    
    (m,c) = kmeans(image, cluster_number, 30) 
    
    fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 6))
    fig.suptitle("K-means clustering with "+str(cluster_number)+" clusters", fontsize = 14)
    
    ax[0].set_title(r'Clustering image ('+str(cluster_number)+" clusters)", fontsize = 13)
    ax[0].imshow(m, cmap ='jet', vmin = vmin, vmax= vmax)

    ax[1].set_title(r'Loading plot', fontsize = 13)
    for i in range(c.shape[0]):
        ax[1].plot(c[i])
    
    
    fig.tight_layout()
    plt.show()
    
    
# 2-clusters, 30-no of iterations--On the selected PCs
k_means_analysis(img_pc, 2, vmin=0, vmax=1)

# 3-clusters, 30-no of iterations--On the selected PCs
k_means_analysis(img_pc, 3, vmin=1, vmax=2)

# 4-clusters, 30-no of iterations--On the selected PCs
k_means_analysis(img_pc, 4, vmin=1, vmax=3)

# 5-clusters, 30-no of iterations--On the selected PCs
k_means_analysis(img_pc, 5, vmin=1, vmax=4)

# 5-clusters, 30-no of iterations--On the Original image
k_means_analysis(hyperim, 5, vmin=0, vmax=2)




#creating the ground truth image
shape = hyperim.shape
groundtruth = np.zeros([shape[0],shape[1]])
groundtruth[280:300, 255:285] = 1.0   #grass
groundtruth[250:270, 300:320] = 6.0   #dark tree
groundtruth[80:100, 145:165] = 2.0 # asphalt--road-light
groundtruth[270:280, 190:200] = 3.0 # road-dark narrow
groundtruth[155:175,230:250] =4.0 #brown roof
groundtruth[305:325, 125:145] =5.0 #dark roof left


#displaying the ground truth image
plt.figure()
plt.title("Ground truth")
plt.imshow(groundtruth)
plt.show

# Gaussian Maximum Likelihood classification
classes = create_training_classes(hyperim, groundtruth)
gmlc = GaussianClassifier(classes)
clmap = gmlc.classify_image(hyperim)


imshow(classes=clmap, figsize=(12,8))
plt.title("Gaussian Maximum Likelihood classification")
plt.show()