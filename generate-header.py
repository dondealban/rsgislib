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

        # Change to file directory (can work with relative paths)
        os.chdir(inFileDIR)

        # Get name for all expected files
        inHHFileList = glob.glob('*HH')
        inHVFileList = glob.glob('*HV')
        inDateFileList = glob.glob('*_date')
        inIncFileList = glob.glob('*_linci')
        inMaskFileList = glob.glob('*_mask')
        inHeaderFileList = glob.glob('KC*.hdr')

        if len(inHeaderFileList) == 1:
            inHeaderFile = inHeaderFileList[0]
        else:
            raise Exception('Could not find header.')

        # Open JAXA header file for reading (r)
        inHeader = open(inHeaderFile, 'r')

        inULat = ''
        inULon = ''

        # Get upper left coordinates from header
        i = 1
        for line in inHeader:
            if i == 13:
                inULat = line.strip()
            elif i == 14:
                inULon = line.strip()
            i+=1

        # Convert degrees to minutes
        inULat = str(int(inULat) * 3600)
        inULon = str(int(inULon) * 3600)

        # Close header file
        inHeader.close()

        # Set up string with header information for 16-bit image
        headerText = '''ENVI
description = {
 %s}
samples = 4500
lines   = 4500
bands   = 1
header offset = 0
file type = ENVI Standard
data type = 12
interleave = bsq
sensor type = Unknown
byte order = 0
map info = {Geographic Lat/Lon, 1.0000, 1.0000, %s, %s, 8.0000000000e-01, 8.0000000000e-01, WGS-84, units=Seconds}
wavelength units = Unknown
''' %(inHeaderFile, inULon, inULat)

        # Set up string with header information for 8-bit ancillary files
        headerTextByte = '''ENVI
description = {
 %s}
samples = 4500
lines   = 4500
bands   = 1
header offset = 0
file type = ENVI Standard
data type = 1
interleave = bsq
sensor type = Unknown
byte order = 0
map info = {Geographic Lat/Lon, 1.0000, 1.0000, %s, %s, 8.0000000000e-01, 8.0000000000e-01, WGS-84, units=Seconds}
wavelength units = Unknown
''' % (inHeaderFile, inULon, inULat)

        # Initialise variables to be returned
        inHHFile = None
        inHVFile = None

        # Check if files were found
        # Write header to text file if they were
        if len(inHHFileList) == 1:
            inHHFile = inHHFileList[0]
            inHHHeaderFile = inHHFile + '.hdr'
            inHHHeader = open(inHHHeaderFile, 'w')
            inHHHeader.write(headerText)
            inHHHeader.close()

        if len(inHVFileList) == 1:
            inHVFile = inHVFileList[0]
            inHVHeaderFile = inHVFile + '.hdr'
            inHVHeader = open(inHVHeaderFile, 'w')
            inHVHeader.write(headerText)
            inHVHeader.close()

        if len(inDateFileList) == 1:
            inDateFile = inDateFileList[0]
            inDateHeaderFile = inDateFile + '.hdr'
            inDateHeader = open(inDateHeaderFile, 'w')
            inDateHeader.write(headerText)
            inDateHeader.close()

        if len(inIncFileList) == 1:
            inIncFile = inIncFileList[0]
            inIncHeaderFile = inIncFile + '.hdr'
            inIncHeader = open(inIncHeaderFile, 'w')
            inIncHeader.write(headerText)
            inIncHeader.close()

        if len(inMaskFileList) == 1:
            inMaskFile = inMaskFileList[0]
            inMaskHeaderFile = inMaskFile + '.hdr'
            inMaskHeader = open(inMaskHeaderFile, 'w')
            inMaskHeader.write(headerText)
            inMaskHeader.close()

        # Return names of HH and HV files
        return inHHFile, inHVFile

    def run(self, inDIR):
        """Find files and decompress if extension is .tar.gz and make ENVI header file."""

        fileList = []
        os.chdir(inDIR)

        # List files starting with KC
        fileList = glob.glob('KC*')

        # Iterate through files
        for fileName in fileList:
            print('*** ' + fileName + ' ***')

            baseFile = None # Initialise to None

            # Check if file is .tar.gz, and decompress if it is
            if fileName.find('.tar.gz') > -1:
                baseFile = fileName.replace('.tar.gz', '')
                tarResult = self.unTar(inDIR, baseFile)
            elif os.path.isdir(fileName):
                baseFile = fileName
            else:
                print('Skipping: ' + fileName)

            # If base file has been set, try to create header
            if baseFile is not None:
                try:
                    inHHFile, inHVFile = self.createHeader(os.path.join(inDIR, baseFile))

                    # Print HH and HV file names if they are returned
                    # Could run gdal translate here to convert to other formats
                    # See commented out lines
                    if inHHFile is not None:
                        print(' HH: ', inHHFile)
                        # inHHFilePath = os.path.join(inDIR, baseFile, inHHFile)
                        # gdalCMD = 'gdal_translate -of GTiff -ot Byte -scale 500 4000 {0} {1}'.format(inHHFilePath, inHHFilePath + '.tiff')
                        # subprocess.call(gdalCMD, shell=True)

                    if inHVfile is not None:
                        print(' HV: ', inHVFile)
                except Exception as err:
                    print(err)


