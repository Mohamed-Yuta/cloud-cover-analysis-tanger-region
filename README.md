
# Cloud Cover Analysis in Tanger Region

## Project Overview
This project analyzes Landsat metadata to study cloud cover distribution and trends over the Tanger region. The analysis focuses on filtering data for the Tanger area, visualizing cloud cover, and examining temporal trends.

---

## Dataset
### Source
- Landsat Metadata File: `landsat_ot_c2_l2_67952877dff0cdf1.csv`
- Encoding: `ISO-8859-1`

### Columns Used
1. **Landsat Product Identifier L2**: Unique identifier for each Landsat product.
2. **Date Acquired**: Acquisition date for each scene.
3. **Scene Cloud Cover L1**: Percentage of cloud cover in the scene.
4. **Scene Center Latitude**: Latitude of the scene center.
5. **Scene Center Longitude**: Longitude of the scene center.

---

## Methodology

### 1. Data Preprocessing
- **Encoding Detection**: Used `chardet` to identify the correct encoding (`ISO-8859-1`).
- **Loading Data**: Loaded the Landsat metadata using Pandas.
- **Missing Values**: Dropped rows with missing values in critical columns.

### 2. Filtering for Tanger Region
Defined a bounding box for the Tanger region based on approximate geographic coordinates:
- Latitude: 35.5 to 36.5
- Longitude: -6.5 to -5.0

Filtered the dataset to include only scenes within this bounding box.

### 3. Visualization
- **Cloud Cover Spatial Distribution**:
  - Plotted scene locations colored by cloud cover percentage using Matplotlib.
- **Cloud Cover Trends Over Time**:
  - Visualized temporal trends in cloud cover for the Tanger region.

---

## Results

### Cloud Cover Analysis
- Filtered dataset saved as: `tanger_landsat_data.csv`
- Scatter plot showing cloud cover distribution across scenes in the Tanger region.
- Time-series plot illustrating cloud cover trends over time.

### Key Insights
- Cloud cover data was successfully visualized, revealing spatial and temporal patterns in the Tanger region.
- NDVI could not be calculated due to the absence of Red and NIR band reflectance values.

---

## Challenges
1. Lack of reflectance bands (e.g., Red, NIR, SWIR1) in the dataset.
2. No shapefile available for the Tanger region, so a bounding box was used instead.

---

## Recommendations

### For Further Analysis
1. **Obtain Surface Reflectance Data**:
   - Download Landsat Level-2 data from USGS Earth Explorer.
   - Ensure the dataset includes bands for NDVI or NDBI calculation.

2. **Google Earth Engine**:
   - Use GEE to calculate NDVI or NDBI for multiple years and perform temporal analysis.

3. **Incorporate Shapefiles**:
   - Use a shapefile for precise geographic filtering and visualization.

### Possible Enhancements
- Perform urban growth analysis using NDBI if reflectance data becomes available.
- Examine other environmental factors such as vegetation indices or temperature trends.

---

## How to Run
1. Place the Landsat CSV file (`landsat_ot_c2_l2_67952877dff0cdf1.csv`) in the `Data/` directory.
2. Run the Python script (`test.py`) to preprocess the data and generate visualizations.
3. The filtered dataset will be saved as `tanger_landsat_data.csv` in the working directory.

---

## Files
1. **`test.py`**: Python script for data preprocessing and visualization.
2. **`landsat_ot_c2_l2_67952877dff0cdf1.csv`**: Original Landsat metadata.
3. **`tanger_landsat_data.csv`**: Filtered dataset for the Tanger region.

---

## Dependencies
- Python 3.7+
- Libraries:
  - pandas
  - numpy
  - matplotlib
  - chardet

Install dependencies using:
```bash
pip install pandas numpy matplotlib chardet
```

---

## Contact
For further questions or feedback, please reach out to the project author.
