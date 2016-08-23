# ----------------------------------------------------------------------
# This Python script calibrates L-band SAR mosaic data, both JERS-1 and
# ALOS/PALSAR, to normalised radar cross-section. This script is a
# modified version based on the original script developed by Dr Peter
# Bunting and Dr Daniel Clewley for the JAXA K&C 20 Global Mangrove
# Watch Workshop.
#
# Script modified by:   Jose Don T. De Alban
# Date created:         23 Aug 2016
# Last modified:
# ----------------------------------------------------------------------

# !/usr/bin/env python

# Import OS module
import os

# Import glob module
import glob

#Import RSGISLib modules
import rsgislib
from rsgislib import imagecalc
from rsgislib import imageutils

# Set output data type and format
outputFormat = 'KEA'
outputType = rsgislib.TYPE_32UINT

# Define calibration expressions for JERS-1 and ALOS/PALSAR datasets
jers1Cal = '10^(2*log10(b1) - 8.466)'
palsarCal = '10^(2*log10(b1) - 8.3)'

# Get list of JERS-1 and ALOS/PALSAR scenes
jers1ImageList = glob.glob("*JERS1*_utm_sub.kea")
palsarImageList = glob.glob("*PALSAR_*_utm_sub.kea")

# Iterate through JERS-1 files
for jers1Image in jers1ImageList
    print('Calibrating: ' + jers1Image)

    # Set name for output images by replacing '.kea' with '_cal.kea'
    outputImage = jers1Image.replace('.kea','_cal.kea')

