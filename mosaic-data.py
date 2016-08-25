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
import subprocess

