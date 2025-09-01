## Hyperspectral Image Analysis – Vegetation Identification 🌱

### Task  
Analyze the hyperspectral image `sandvika.npy` to explore different methods for **vegetation detection and classification**, including NDVI, PCA, and K-means clustering.

![Assignment 3 Preview](Assignments/Assignment03/A3.png)


### Workflow  
1. **Loading Data**  
   - Read hyperspectral cube (`.npy`) and corresponding header (`Visnir.hdr`).  
   - Identify required wavelength bands for Blue (440 nm), Green (535 nm), Red (645 nm), and NIR (800 nm).  

2. **RGB Visualization**  
   - Create RGB images using single bands.  
   - Enhance visualization by averaging across multiple bands for each color channel.  

3. **NDVI Calculation**  
   - Compute NDVI using both formula and built-in functions.  
   - Generate NDVI maps where values range from `-1 to 1` (healthy vegetation ≈ 0.66–1).  
   - Threshold NDVI to highlight only **healthy vegetation**.  

4. **Spectral Analysis**  
   - Extract spectra for vegetation, asphalt, and rooftops.  
   - Compare reflectance across wavelengths to confirm vegetation signatures (red-edge rise beyond 680 nm).  

5. **PCA (Principal Component Analysis)**  
   - Perform PCA on the hyperspectral cube.  
   - Visualize variance explained and PCA score images.  
   - Interpret loadings to identify wavelength contributions.  
   - PCA successfully separates vegetation (grass, trees) from man-made surfaces.  

6. **K-means Clustering**  
   - Apply unsupervised clustering (k=2–5) on PCA-reduced data.  
   - Identify vegetation, rooftops, and roads.  
   - Best separation observed at **k=5**, but some confusion remained between trees and rooftops.  

### Findings  
- **NDVI & NDVI Thresholding** – Simple and effective for identifying vegetation but cannot differentiate vegetation types.  
- **PCA** – Best option for both detecting and classifying different vegetation (grass vs. trees).  
- **K-means** – Useful for separating major classes but misclassifies some vegetation and rooftops.  

### Conclusion  
📌 Among all methods, **PCA** is the most appropriate for vegetation classification in this hyperspectral dataset, while **NDVI thresholding** remains the simplest approach for vegetation detection.  

---

📄 *This project was part of the **INF250 Image Processing** course assignments.*
