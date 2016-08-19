# ----------------------------------------------------------------------
# This Python script subsets multiple files using a bounding box vector,
# which is a modified version based on the original script developed by
# Dr Peter Bunting and Dr Daniel Clewley for the JAXA K&C 20 Global
# Mangrove Watch Workshop.
#
# Script modified by:   Jose Don T. De Alban
# Date created:         19 Aug 2016
# Last modified:
# ----------------------------------------------------------------------

# !/usr/bin/env python

# Import glob module
import glob

# Import required RSGISLib modules
import rsgislib
from rsgislib import imageutils

# Set input bounding box vector for all files
inputVector = 'bounding_box_utm.shp'

