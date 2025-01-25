import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Detect file encoding
import chardet
with open("Data/landsat_ot_c2_l2_67952877dff0cdf1.csv", "rb") as file:
    result = chardet.detect(file.read(10000))
    print(result)

landsat_csv = "Data/landsat_ot_c2_l2_67952877dff0cdf1.csv"

# Load the CSV with the detected encoding
landsat_data = pd.read_csv(landsat_csv, encoding="ISO-8859-1")

# Display basic information
print("First few rows of the dataset:")
print(landsat_data.head())
print("Columns in the dataset:")
print(landsat_data.columns)
print("Basic dataset information:")
print(landsat_data.info())

# Select specific columns
selected_columns = [
    "Landsat Product Identifier L2",
    "Date Acquired",
    "Scene Cloud Cover L1",
    "Scene Center Latitude",
    "Scene Center Longitude"
]
landsat_filtered = landsat_data[selected_columns]

# Filter data for the Tanger region based on latitude and longitude bounds
# Approximate bounding box for Tanger (latitude: 35.5 to 36.5, longitude: -6.5 to -5.0)
landsat_tanger = landsat_filtered[
    (landsat_filtered["Scene Center Latitude"] >= 35.5) &
    (landsat_filtered["Scene Center Latitude"] <= 36.5) &
    (landsat_filtered["Scene Center Longitude"] >= -6.5) &
    (landsat_filtered["Scene Center Longitude"] <= -5.0)
]

# Drop missing values
landsat_tanger_cleaned = landsat_tanger.dropna()

# Plot cloud cover over Tanger region
plt.figure(figsize=(10, 6))
plt.scatter(
    landsat_tanger_cleaned["Scene Center Longitude"],
    landsat_tanger_cleaned["Scene Center Latitude"],
    c=landsat_tanger_cleaned["Scene Cloud Cover L1"],
    cmap="viridis",
    s=50
)
plt.colorbar(label="Scene Cloud Cover (%)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Landsat Scenes with Cloud Cover (Tanger Region)")
plt.show()
# Save the filtered data
landsat_tanger_cleaned.to_csv("tanger_landsat_data.csv", index=False)
print("Filtered data saved as 'tanger_landsat_data.csv'.")

# Convert "Date Acquired" to datetime
landsat_tanger_cleaned["Date Acquired"] = pd.to_datetime(landsat_tanger_cleaned["Date Acquired"])

# Plot cloud cover over time
plt.figure(figsize=(10, 6))
plt.plot(
    landsat_tanger_cleaned["Date Acquired"],
    landsat_tanger_cleaned["Scene Cloud Cover L1"],
    marker="o"
)
plt.title("Cloud Cover Trends Over Time (Tanger Region)")
plt.xlabel("Date Acquired")
plt.ylabel("Cloud Cover (%)")
plt.grid(True)
plt.show()

