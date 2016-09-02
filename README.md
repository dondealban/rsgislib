# rsgislib
This repository contains modified Python scripts that utilise the Remote Sensing and GIS software library (RSGISLib) for processing JAXA's SAR mosaic image datasets. These are based on the original scripts developed by Dr Peter Bunting (Aberystwyth University) and Dr Daniel Clewley (University of Southern California) for the Global Magrove Watch Workshop during the 20th Science Team Meeting of the Kyoto & Carbon Initiative on December 2013 held in Tokyo, Japan. For more information about RSGISLib, please visit: http://www.rsgislib.org/index.html

A brief description of the scripts is as follows including the order of execution:

*For working with JERS-1/PALSAR mosaics provided through K&C Initiative, these scripts should be executed first:*

* untar-files.py -- decompresses the tar.gz file into a directory with the same name as the tar.gz file
* generate-header.py -- decompresses tar.gz file into a directory and creates header files for each image inside

*For working with mosaics downloaded through the JAXA portal (http://www.eorc.jaxa.jp/ALOS/en/palsar_fnf/data/index.htm), note that the images within tar.gz files already contain header files. Hence, the generate-header.py can be skipped. The scripts may be executed as follows:*

* untar-files.py -- decompresses the tar.gz file into a directory with the same name as the tar.gz file
* mosaic-data.py -- creates a mosaic image using the input parameters set at command line

subset-files.py -- creates a subset
calibrate-data.py -
