# ----------------------------------------------------------------------
# This Python script generates ENVI header files for L-band SAR
# mosaic data, both JERS-1 and ALOS/PALSAR. This script is a modified
# version of the original script developed by Dr Daniel Clewley
# for the JAXA K&C 20 Global Mangrove Watch Workshop.
#
# Script modified by:   Jose Don T. De Alban
# Date created:         23 Aug 2016
# Last modified:
# ----------------------------------------------------------------------

# !/usr/bin/env python

# Import required modules
import subprocess, os, sys, glob

