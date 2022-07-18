#!/usr/bin/python
#
# Extracts all the spot weights from a proton DICOM plan saved as a text file
# Created by Francesca Fiorini 17/09/2019
#
# Modified by Jamil Lambert 15/11/2019:
#    changed the output file name to contain the beam ID
#    one file is created per beam in the DICOM plan

filename = 'rtplan.txt' #DICOM plan must be saved as text by exporting from DVTk DICOM editor into this file in the working directory

new_filename = 'ff0_file.txt' #temporary file, deleted after run

import re
import math

from tempfile import mkstemp
from shutil import move
from os import remove, close

def replace(file_path,new_file_path):
    #Create new file
    new_file = open(new_file_path,'w')
    old_file = open(file_path)
    for line in old_file:
        line = line.replace("[", ",")
        line = line.replace("\t", ",")
        line = line.replace(']', ',')
        line = line.replace('\\', ',')
        line = line.replace('>', ' ')        
        line = line.replace('#', ' ')
        line = line.replace('0x', ' ')
        line = line.replace('Nominal Beam Energy', ' ')
        line = line.replace('Scan Spot Meterset Weights', ' ')
        line = line.replace('DS,', ' ')
        line = line.replace('FL,', ' ')        
        new_file.write(line)
    #close new file
    new_file.close()
    old_file.close()

replace(filename,new_filename)

with open(new_filename) as myfile:
    for line in myfile:
        if re.match('    300a00c2,,LO,,', line):  #gets beam ID
            weights_filename = 'weights_' + line[18:23] + '.txt'
            ff1_file = open(weights_filename,"w+")
        if re.match('       300a0114,, ,', line):  #select energy lines
             for item in line.split(','):
                try:
                    value = float(item)
                    ff1_file.write(str(value) + ' ')
                except ValueError:
                    # if it fails, it's a string.
                    continue
             ff1_file.write('\n')

        if re.match('       300a0396,, ,', line):
#            print line
            for item in line.split(','):
                try:
                    value = float(item)
                    ff1_file.write(str(value) + ' ')
                except ValueError:
                    # if it fails, it's a string.
                    continue
            ff1_file.write('\n')
            
ff1_file.close()
remove(new_filename)

