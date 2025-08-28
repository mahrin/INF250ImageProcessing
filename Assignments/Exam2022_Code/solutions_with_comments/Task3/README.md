# Exercise 3 – Hyperspectral Image Analysis (nmbu.npy)

### Part (a) – Load & Display (5p)
- Load `nmbu.npy` and `nmbu.hdr`.  
- Display RGB by selecting 3 wavebands (report bands + wavelengths).  

### Part (b) – Spectral Plot (5p)
- Plot spectrum vs. wavelength for:  
  - Grass  
  - Asphalt  
  - Black roof  
  - Red roof  
  - Solar panels  
  - Water  

### Part (c) – NDVI (5p)
- Compute and display **NDVI image**.  

### Part (d) – PCA (15p)
- Compute PCA.  
- Display 5 score images + loadings, interpret observations.  
- Plot Eigenvalues; explain the break at component 2.  
- Report explained variance for first 2 components.  
- State how many components cover 99.9% variance.  

### Part (e) – Gaussian Maximum Likelihood Classification (10p)
- Classify 4–6 classes.  
- Run classification on:  
  1. Full hyperspectral image  
  2. Stack of first 8 PC score images  
- Show ground truth + results.  
- Comment on differences.  

### Part (f) – Vegetation Edge Detection (10p)
- Apply edge detection on vegetation class.  
- Overlay with NDVI image to outline vegetation areas.  
