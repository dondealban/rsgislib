# ----------------------------------------------------------------------
# This Python script subsets multiple files using a bounding box vector,
# which is a modified version based on the original script developed by
# Dr Peter Bunting and Dr Daniel Clewley for the JAXA K&C 20 Global
# Mangrove Watch Workshop.
#
# Script modified by:   Jose Don T. De Alban
# Date created:         19 Aug 2016
# Last modified:        23 Aug 2016
# ----------------------------------------------------------------------

# !/usr/bin/env python

# Import glob module
import glob

# Import required RSGISLib modules
import rsgislib
from rsgislib import imageutils

# Set input bounding box vector for all files
inputVector = 'bounding_box_utm.shp'

# Set output data type and format
outputFormat = 'KEA'
outputType = rsgislib.TYPE_32UINT

# Get list of files in the data directory matching pattern '*_utm.kea'
inputImageList = glob.glob("*_utm.kea")

# Iterate through files within the directory
for inputImage in inputImageList
    print('Subsetting: ' + inputImage)

    # Set name for output subsets by replacing '.kea' with '_sub.kea'
    outputImage = inputImage.replace('.kea','_sub.kea')
    print('Saving to: ' + outputImage)

    # Implement subsetting of images
    imageutils.subset(inputImage, inputVector, outputImage, outputFormat, outputType)

    # Calculate statistics and pyramids for faster display
    imageutils.popImageStats(outputImage, True, 0., True)
    print('Calculating stats\n')