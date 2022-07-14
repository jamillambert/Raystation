# Creates a link to a script located on the clients local computer so that it can be run directly from the scripting menu in Raystation

import sys
sys.path.insert(1, '\\\Client\C$\python') # local directory of the script to be run \\\Client\C$\ is the local c:\
import test # name of the script file without the file extension
