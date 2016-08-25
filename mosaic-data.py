# ----------------------------------------------------------------------
# This Python script creates a mosaic from L-band SAR mosaic tile data,
# both JERS-1 and ALOS/PALSAR, and saves the mosaicked file in KEA file
# format. This script is a modified version of the original script
# developed by Dr Daniel Clewley for the JAXA K&C 20 Global Mangrove
# Watch Workshop.
#
# Usage: script should be in the same directory where the uncompressed
# mosaic tile folders are located.
#
# Script modified by:   Jose Don T. De Alban
# Date created:         25 Aug 2016
# Last modified:
# ----------------------------------------------------------------------

# !/usr/bin/env python

# Import required modules
import os, glob

# Get list of files matching the following file name patterns
# inputImageList = glob.glob("*HH*")

# Iterate through files within the directory
# for inputImage in inputImageList
#    print('Subsetting: ' + inputImage)
#    Set name for output subsets by replacing '.kea' with '_sub.kea'
#    outputImage = inputImage.replace('.kea','_sub.kea')

# Create text file that will contain list of specific file names
fileList = open('filelist.txt', 'w')

# Search for specific files within directories then write file names in text file
for root, dirs, files in os.walk('*HH_F02DAR'):
    for targetfile in files:
        filename = os.path.join(targetfile)
        filestring = filename + '\n'
        fileList.write(filestring)
        print(filestring)


