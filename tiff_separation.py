#This code has been tested under python ver 3.7.

import os
import rasterio

# Set the output folder
output_folder = r"C:\path\output" #Specify where you want to store the output file

# Check if the output folder exists
if os.path.exists(output_folder):
    # Use the existing folder
    print(f'Using existing folder: {output_folder}')
else:
    # Create the output folder
    os.makedirs(output_folder)
    print(f'Created new folder: {output_folder}')

# Open the input file
with rasterio.open(r"C:\path\to\input_file") as src: #Specify the path to the concated tiff file
    # Loop through each band in the input file
    for i in range(src.count):
        # Read the band data
        band = src.read(i+1)

        # Create the output file name
        output_file = os.path.join(output_folder, f'output_file_{i+1}.tif')

        # Write the band data to the output file
        with rasterio.open(output_file, 'w', driver='GTiff', width=src.width, height=src.height, count=1, dtype=src.dtypes[0], crs=src.crs, transform=src.transform) as dst:
            dst.write(band, 1)