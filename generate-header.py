# ----------------------------------------------------------------------
# This Python script generates ENVI header files for L-band SAR
# mosaic data, both JERS-1 and ALOS/PALSAR. This script is a modified
# version of the original script developed by Dr Daniel Clewley
# for the JAXA K&C 20 Global Mangrove Watch Workshop.
#
# Usage: script should be in the same directory as the .tar.gz files.
#
# Script modified by:   Jose Don T. De Alban
# Date created:         23 Aug 2016
# Last modified:
# ----------------------------------------------------------------------

# !/usr/bin/env python

# Import required modules
import subprocess, os, sys, glob

class UnTarHeader (object):

    def unTar(self, inDIR, filename):
        """Create directory for file and uncompresses the file to it."""

        # Check if directory exists (if it does assume already uncompressed)
        if not os.path.isdir(os.path.join(inDIR, fileName)):

            # Make a directory
            mkdirCommand = 'mkdir ' + inDIR + '/' + fileName
            subprocess.call(mkdirCommand, shell=True)

            # Copy .tar.gz file to it
            cpCommand = 'cp ' + inDIR + '/' + fileName + '.tar.gz' + inDIR + '/' + fileName + '/'
            subprocess.call(cpCommand, shell=True)

            # Change directory
            os.chdir(inDIR + '/' + fileName)

            # Decompress .tar.gz file
            unzipCommand = 'tar -xf ' + fileName + '.tar.gz'
            subprocess.call(unzipCommand, shell=True)

            # Remove .tar.gz file that was copied in the directory
            removeCommand = 'rm ' + fileName + '.tar.gz'
            subprocess.call(removeCommand, shell=True)

    def createHeader (self, inFileDIR):
        """Read in parameters from JAXA header file and writes and ENVI header file."""