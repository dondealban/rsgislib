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
# Last modified:        01 Sep 2016
# ----------------------------------------------------------------------

# !/usr/bin/env python

# Import required modules
import os, fnmatch

# Create text file that will contain list of specific file names
with open('filelist.txt', 'w') as fileList:

# Search for specific files within directories then write file names in text file
for path, subdirs, files in os.walk('.'):
    for targetfile in files:
        targetfile = glob.glob("*HH_F02DAR")
        filename = os.path.join(path, targetfile)
        fileList.write(str(filestring) + os.linesep)



