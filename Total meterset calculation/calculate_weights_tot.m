% Calculates the proton beam meterset weight sum based on the output of the python script:
%    select_weights.py
%
% Created by Francesca Fiorini 17/09/2019
%
% Modified by Jamil Lambert 15/11/2019:
%    changed input file name to match changes in python script
%    removed popup to select directory, sums all files in working directory output by python script
%    rounded output to 6 decimal places to match Pinnacle spot weight accuracy


warning('off','all');
clc
pkg load statistics
format long

myDir = pwd(); %gets directory
myFiles = dir(fullfile(myDir,'weights_*.txt')); %gets all txt files in working directory
for k = 1:length(myFiles)
  baseFileName = myFiles(k).name;
  fullFileName = fullfile(myDir, baseFileName);
  fprintf(1, 'Now reading: %s\n', baseFileName);
  P= importdata(fullFileName,' ');  
  P(isnan(P))=0;
  sizeP = size(P);
  tot_weights =0;
   for i=2:4:sizeP(1)
     tot_weights= tot_weights+ nansum(P(i,:));
   end
  fprintf(1, '>(300a,010e) Final Cumulative Meterset Weight: %.6f\n\n', tot_weights);   %outputs the total meterset weight

end

