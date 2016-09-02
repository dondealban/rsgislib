# ----------------------------------------------------------------------
# This Python script creates a mosaic from L-band SAR mosaic tile data,
# both JERS-1 and ALOS/PALSAR, and saves the mosaicked file in KEA file
# format. It recursively finds files in a given directory with a given
# search string, and then proceeds to produce a mosaic of those files.
#
# This script is a duplicate of the original script by Dr Daniel Clewley
# developed for the Remote Sensing and GIS Software Library (RSGISLib).
# It is reproduced here with slight modifications for use in my own
# research. Please see copy of the copy of the original license which is
# reproduced above for more information.
#
# Usage: script should be in the same directory where the uncompressed
# mosaic tile folders are located.
#
# Script modified by:   Jose Don T. De Alban
# Date created:         25 Aug 2016
# Last modified:        02 Sep 2016
#
# ----------------------------------------------------------------------
#
# rsgislibmosaic.py
#
# RSGISLib: 'The remote sensing and GIS Software Library'
#
# RSGISLib is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# RSGISLib is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with RSGISLib. If not, see <http://www.gnu.org/licenses/>.
#
# Author:   Dan Clewley
# Email:    daniel.clewley[at]gmail.com
# Date:     28/08/2013
# Version:  1.0
#
# ----------------------------------------------------------------------

# !/usr/bin/env python

# Import required modules
import os, sys
import argparse
import fnmatch
import rsgislib
from rsgislib import imageutils


# Define functions
def getRSGISLibDataType(gdaltype):
    gdaltype = gdaltype.lower()
        if gdaltype == 'byte' or gdaltype =='int8':
            return rsgislib.TYPE_8INT
        elif gdaltype == 'int16':
            return rsgislib.TYPE_16INT
        elif gdaltype == 'int32':
            return rsgislib.TYPE_32INT
        elif gdaltype == 'int64':
            return rsgislib.TYPE_64INT
        elif gdaltype == 'uint8':
            return rsgislib.TYPE_8UINT
        elif gdaltype == 'uint16':
            return rsgislib.TYPE_16UINT
        elif gdaltype == 'uint32':
            return rsgislib.TYPE_32UINT
        elif gdaltype == 'uint64':
            return rsgislib.TYPE_64UINT
        elif gdaltype == 'float32':
            return rsgislib.TYPE_32FLOAT
        elif gdaltype == 'float64':
            return rsgislib.TYPE_64FLOAT

def getGDALFormat(filename):
    """Get GDAL format based on filename."""
    gdalStr = ''
    extension = os.path.splitext(filename)[-1]
    if extension == '.env':
        gdalStr = 'ENVI'
    elif extension == '.kea':
        gdalStr = 'KEA'
    elif extension == '.tif':
        gdalStr = 'GTiff'
    elif extension == '.img':
        gdalStr = 'HFA'
    else:
        raise exception('Type not recognised.')
    return gdalStr




# Create text file that will contain list of specific file names
with open('filelist.txt', 'w') as fileList:

# Search for specific files within directories then write file names in text file
for path, subdirs, files in os.walk(inDIR):
    for targetfile in files:
        if fnmatch.fnmatch(targetfile, pattern): # Match search string
            fileList.append(os.path.join(path, targetfile))
        # targetfile = glob.glob("*HH_F02DAR")
        # filename = os.path.join(path, targetfile)
        # fileList.write(str(filestring) + os.linesep)



