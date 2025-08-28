# Importing all the necessary modules
from spectral import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as m
import skimage
import math


# Function for finding the required bands
def find_bands(all_wavelengths, required_wavelengths):
    """
    Parameters:
        all_wavelengths: list of all 186 wavelengths available
        required_wavelengths:  a dictionary which has band names as keys and wavelength as values.
    Return:
        required_bands: a dictionary which has band names as keys and band number as values
    """
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
                    band = index  

            band_name = required_wavelengths[wavelength]
            required_bands[band_name]=band        
    return required_bands


#Loading the image
hyperim = np.load("nmbu.npy")


# Calling the function to get required wavelength bands
wavelength = envi.read_envi_header('nmbu.hdr')['wavelength']
default_bands = envi.read_envi_header('nmbu.hdr')['default_bands']
all_wavelengths = [float(i) for i in wavelength]
required_wavelengths = {440:"blue", 535:'green', 645:'red', 800:'NIR'}
required_bands = find_bands(all_wavelengths, required_wavelengths)
print("Wavelength available:", len(wavelength))
print("Required_bands", required_bands)
print("Default_bands", default_bands)


#Organising the RGB bands in list format
print("required_bands", required_bands)   
RGB_bands = [required_bands['red'],required_bands['green'],required_bands['blue']]
print("RGB_bands", RGB_bands)
NIR_band = required_bands['NIR']
print("NIR_band", NIR_band)
red_band = required_bands['red']
print("red_band", red_band)


imshow(hyperim, bands = RGB_bands, stretch=((0.02,0.98),(0.02,0.98),(0.02,0.98)), figsize=(10,6))
plt.title("RGB image with 1 band for each color")
plt.show()