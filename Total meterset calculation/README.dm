Original scripts (calculate_weights_tot.m, and select_weights.py) by Francesca Fiorini
Modified by Jamil Lambert to split weight calc per beam and created a batch file to run scripts sequentially

To run open the dicom plan with DCM Editor and export as a text file
name the text file rtplan.txt and place in the same directory as the scripts
run the batch file
In dcm Editor find the tag ">(300a,010e) Final Cumulative Meterset Weight" for each beam and change it to the value given by the script.  Only the digits after the decimal place should change, if the value before the decimal is different do not chagne it since something has gone wrong.