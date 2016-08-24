# ----------------------------------------------------------------------
# This Python script decompresses .tar.gz files containing L-band SAR
# mosaic data, both JERS-1 and ALOS/PALSAR, and saves the files in a
# directory. This script is a modified version of the original script
# developed by Dr Daniel Clewley for the JAXA K&C 20 Global Mangrove
# Watch Workshop.
#
# Usage: script should be in the same directory as the .tar.gz files.
#
# Script modified by:   Jose Don T. De Alban
# Date created:         24 Aug 2016
# Last modified:
# ----------------------------------------------------------------------

# !/usr/bin/env python

# Import required modules
import subprocess, os, sys, glob

class UnTarFile (object):

    def unTar(self, inDIR, fileName):
        """Create directory for file and uncompress the file into it."""

        # Check if directory exists (if it does assume already uncompressed)
        if not os.path.isdir(os.path.join(inDIR, fileName)):

            # Make a directory
            mkdirCommand = 'mkdir ' + inDIR + '/' + fileName
            subprocess.call(mkdirCommand, shell=True)

            # Copy .tar.gz file to it
            cpCommand = 'cp ' + inDIR + '/' + fileName + '.tar.gz ' + inDIR + '/' + fileName + '/'
            subprocess.call(cpCommand, shell=True)

            # Change directory
            os.chdir(inDIR + '/' + fileName)

            # Decompress .tar.gz file
            unzipCommand = 'tar -xf ' + fileName + '.tar.gz'
            subprocess.call(unzipCommand, shell=True)

            # Remove .tar.gz file that was copied in the directory
            removeCommand = 'rm ' + fileName + '.tar.gz'
            subprocess.call(removeCommand, shell=True)

if __name__ == '__main__':

    # Check if an input directory has been passed in, and do not run if it has not
    if len(sys.argv) >= 2:
        inDIR = os.path.abspath(sys.argv[1])
    else:
        print('''Not enough parameters provided.
Usage:
    python untar-files.py inDIR
''')
        sys.exit()

    obj = UnTarFile()